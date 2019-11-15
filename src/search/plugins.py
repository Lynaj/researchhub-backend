import base64
import requests
import json

from django.core.exceptions import ImproperlyConfigured
from smart_open import open

from .exceptions import ElasticsearchPluginError
from paper.models import Paper
from researchhub.settings import ELASTICSEARCH_DSL
import utils.sentry as sentry
from utils.http import http_request, RequestMethods as methods


class IngestPdfPipeline:
    def __init__(self):
        self.host = ELASTICSEARCH_DSL.get('default').get('hosts')
        self.url = self.host + f'/_ingest/pipeline/pdf'
        self._build_pipeline_if_not_exists()

    def attach_pdf_to_document(self, index, paper):
        """Encodes the `paper` file and adds it to Elasticsearch.

        Arguments:
            index (str) -- name of the index where the document is located
            paper (obj) -- Paper object to get and add the pdf

        Return:
            response (requests.Response) -- result of attachment put request

        """
        url = self.host + f'/{index}/_doc/{paper.id}?pipeline=pdf'
        pdf = self.encode_file(paper.file.url)
        data = {
            'filename': paper.file.name,
            'pdf': pdf.decode('utf-8')
        }
        headers = {'Content-Type': 'application/json'}
        return self._send_put_request(
            url,
            data,
            headers,
            'Failed to index pdf'
        )

    def encode_file(self, url):
        with open(url, 'rb') as f:
            return base64.b64encode(f.read())

    def _build_pipeline_if_not_exists(self):
        if self._check_pipeline_exists() is False:
            self._build_pipeline()

    def _check_pipeline_exists(self):
        response = http_request(methods.GET, self.url)
        if response.status_code == 200:
            return True
        if response.status_code == 404:
            return False
        raise ElasticsearchPluginError(
            None,
            f'Check pipeline failed with status code {response.status_code}'
        )

    def _build_pipeline(self):
        description = 'Extract pdf attachment'
        processors = [{'attachment': {'field': 'pdf'}}]
        data = {'description': description, 'processors': processors}
        headers = {'Content-Type': 'application/json'}
        self._send_put_request(
            self.url,
            data,
            headers,
            'Failed to add attachment to pipeline'
        )

    def _send_put_request(self, url, data, headers, error_message):
        try:
            response = http_request(
                methods.PUT,
                url,
                json.dumps(data),
                headers=headers
            )
            if not response.ok:
                message = (
                    f'Request to Elasticsearch failed with'
                    f'{response.status_code}'
                )
                sentry.log_error(
                    response.text,
                    message
                )
            return response
        except Exception as e:
            raise ElasticsearchPluginError(e, error_message)


pdf_pipeline = IngestPdfPipeline()