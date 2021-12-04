from rest_framework import generics, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.db.models import Sum, Count
import json

# import Response from rest_framework

from billing.models import SERVICES_CHOICES, Payable, Transaction
from billing.api.serializers import PayableSerializer, TransactionSerializer, FilteredPayableSerializer


""" FILTERS"""

class PayableFilter(filters.FilterSet):
    service = filters.ChoiceFilter(choices=SERVICES_CHOICES)
    class Meta:
        model = Payable
        fields = ['service']


class TransactionFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    class Meta:
        model = Transaction
        fields = ['date']

""" VIEWS """

class PayableList(generics.ListCreateAPIView):
    queryset = Payable.objects
    serializer_class = PayableSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PayableFilter

    def get_serializer_class(self):
        if self.request.query_params.get('service', None) is not None:
            return FilteredPayableSerializer
        else:
            return PayableSerializer

    def get_queryset(self):
        return self.queryset.filter(state=0)


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects
    serializer_class = TransactionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TransactionFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response(
            data= {
                'transaction_set': TransactionSerializer(queryset, many=True).data,
                'total_amount' : queryset.aggregate(Sum('amount')).get('amount__sum'),
                'count' : queryset.count()
            },
            status=status.HTTP_200_OK
        )
