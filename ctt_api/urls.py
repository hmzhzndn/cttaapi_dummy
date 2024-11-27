from django.urls import path
from .views import TransferDataView

urlpatterns = [
    path('transfer/', TransferDataView.as_view(), name='transfer_data'),
]
