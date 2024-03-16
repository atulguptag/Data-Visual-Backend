from django.urls import path
from core.views import GetData

urlpatterns = [
    path('data/', GetData.as_view(), name='GetData'),
]
