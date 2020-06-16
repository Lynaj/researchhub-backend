from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reputation.lib import FIRST_WITHDRAWAL_MINIMUM, get_user_balance
from reputation.models import Withdrawal
from reputation.serializers import WithdrawalSerializer
from user.serializers import UserSerializer
from utils.permissions import CreateOrReadOnly


class WithdrawalViewSet(viewsets.ModelViewSet):
    queryset = Withdrawal.objects.all()
    serializer_class = WithdrawalSerializer
    permission_classes = [IsAuthenticated, CreateOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Withdrawal.objects.all()
        else:
            return Withdrawal.objects.filter(user=user)

    def create(self, request):
        user = request.user
        user_balance = get_user_balance(user)
        if self._check_meets_withdrawal_minimum(user, user_balance):
            response = super().create(request)
            withdrawal_id = response.data['id']
            withdrawal = Withdrawal.objects.get(pk=withdrawal_id)
            serialized = WithdrawalSerializer(withdrawal)
            return Response(serialized.data, status=201)
        else:
            message = f'Insufficient balance of {user_balance}'
            if user_balance > 0:
                message = (
                    f'Balance {user_balance} is below the withdrawal minimum'
                    f' of {FIRST_WITHDRAWAL_MINIMUM}'
                )
            return Response(message, status=400)

    def list(self, request):
        # TODO: Do we really need the user on this list? Can we make some
        # changes on the frontend so that we don't need to pass the user here?
        resp = super().list(request)
        resp.data['user'] = UserSerializer(request.user).data
        return resp

    def _check_meets_withdrawal_minimum(self, user, balance):
        if user.withdrawals.count() < 1:
            return balance >= FIRST_WITHDRAWAL_MINIMUM
        return balance > 0
