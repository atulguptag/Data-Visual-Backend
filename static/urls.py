from django.urls import path
from core.views import GetData, AddData

urlpatterns = [
    path('data/', GetData.as_view(), name='GetData'),
    path('data/add/', AddData.as_view(), name='add_data'),
]
