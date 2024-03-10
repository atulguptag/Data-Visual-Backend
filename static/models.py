# models.py

import json
from django.db import models
from datetime import datetime

# Create your models here.

class DataItem(models.Model):
    end_year = models.CharField(default="", max_length=5, null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=10)
    topic = models.CharField(max_length=50, null=True, blank=True)
    insight = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=500)
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=5, null=True, blank=True)
    impact = models.CharField(max_length=5, null=True, blank=True)
    added = models.CharField(max_length=50)
    published = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=1000)
    likelihood = models.IntegerField(null=True, blank=True)

def load_json_data_into_model():
    with open('jsondata.json', 'r', encoding='utf-8-sig') as f:
        json_data = json.load(f)
        for item in json_data:
            # added_date = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S') if item.get('added', '').strip() else datetime(1900, 1, 1, 0, 0)
            # published_date = datetime.strptime(item['published'], '%B, %d %Y %H:%M:%S') if item.get('published', '').strip() else datetime(1900, 1, 1, 0, 0)
            model_instance = DataItem(
                end_year=item['end_year'],
                intensity=int(item['intensity']),
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'],
                region=item['region'],
                start_year=item['start_year'],
                impact=item['impact'],
                added=item['added'],
                published=item['published'],
                country=item['country'],
                relevance=int(item['relevance']),
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=int(item['likelihood']),
            )
            model_instance.save()

# load_json_data_into_model()