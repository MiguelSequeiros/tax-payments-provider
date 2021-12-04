#register listcreateapiviews
from django.urls import path
from billing.api.views import PayableList, TransactionList

# register the urls
urlpatterns = [
    path('payables/', PayableList.as_view(), name='payable-list'),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
]