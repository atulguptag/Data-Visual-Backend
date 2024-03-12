import os, json
from .models import DataItem
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class GetData(APIView):
    def get(self, request, format=None):
        # Retrieve data from the database
        try:
            data = DataItem.objects.all().values()
            return JsonResponse(list(data), safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Server error'}, status=500)
