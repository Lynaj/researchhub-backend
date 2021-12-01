import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'test')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'NOT_REAL')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'NOT_REAL')

INFURA_PROJECT_ID = os.environ.get('INFURA_PROJECT_ID', 'NOT_REAL')
INFURA_PROJECT_SECRET = os.environ.get('INFURA_PROJECT_SECRET', 'NOT_REAL')
INFURA_RINKEBY_ENDPOINT = f'https://rinkeby.infura.io/v3/{INFURA_PROJECT_ID}'

ORCID_CLIENT_ID = os.environ.get('ORCID_CLIENT_ID', 'NOT_REAL')
ORCID_CLIENT_SECRET = os.environ.get('ORCID_CLIENT_SECRET', 'NOT_REAL')
ORCID_ACCESS_TOKEN = os.environ.get('ORCID_ACCESS_TOKEN', 'NOT_REAL')

MAILCHIMP_KEY = os.environ.get('MAILCHIMP_KEY', 'NOT_REAL')
MAILCHIMP_LIST_ID = os.environ.get('MAILCHIMP_LIST_ID', 'NOT_REAL')

RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY', 'NOT_REAL')

SIFT_ACCOUNT_ID = os.environ.get('SIFT_ACCOUNT_ID', 'NOT_REAL')
SIFT_REST_API_KEY = os.environ.get('SIFT_REST_API_KEY', 'NOT_REAL')
SIFT_WEBHOOK_SECRET_KEY = os.environ.get('SIFT_WEBHOOK_SECRET_KEY', 'NOT_REAL')

AMPLITUDE_API_KEY = os.environ.get('AMPLITUDE_API_KEY', 'NOT_REAL')

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', 'NOT_REAL')

SENTRY_DSN = os.environ.get('SENTRY_DSN', 'NOT_REAL')

APM_URL = os.environ.get('APM_URL', 'NOT_REAL')

ELASTICSEARCH_HOST = os.environ.get('ELASTICSEARCH_HOST', 'NOT_REAL')

CKEDITOR_CLOUD_ACCESS_KEY = os.environ.get('CKEDITOR_CLOUD_ACCESS_KEY', 'NOT_REAL')
CKEDITOR_CLOUD_ENVIRONMENT_ID = os.environ.get('CKEDITOR_CLOUD_ENVIRONMENT_ID', 'NOT_REAL')