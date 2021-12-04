from rest_framework import serializers
from billing.models import Payable, Transaction


class FilteredPayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = ('barcode', 'amount', 'deadline')


class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields  = ('barcode', 'amount', 'deadline', 'service')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields  = ('__all__')

