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

def read_json_data(file_path):
    file_path = os.path.join(settings.BASE_DIR, file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

class AddData(APIView):
    def add(self, request, format=None):
        try:
            new_data = DataItem(**request.POST.dict())
            new_data.save()
            return JsonResponse(new_data.__dict__, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Server error'}, status=500)

data = read_json_data('jsondata.json')