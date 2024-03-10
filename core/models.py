# models.py

import json
from django.db import models
from datetime import datetime

# Create your models here.

class DataItem(models.Model):
    end_year = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField(default=0, null=True, blank=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=50, null=True, blank=True)
    insight = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=500)
    region = models.CharField(max_length=100)
    start_year = models.IntegerField(default=0, null=True, blank=True)
    impact = models.IntegerField(default=0, null=True, blank=True)
    added = models.CharField(max_length=500)
    published = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    relevance = models.IntegerField(default=0, null=True, blank=True)
    pestle = models.CharField(max_length=1000)
    source = models.CharField(max_length=500)
    title = models.CharField(max_length=1000000)
    likelihood = models.IntegerField(default=0, null=True, blank=True)

def load_json_data_into_model():
    with open('jsondata.json', 'r', encoding='utf-8-sig') as f:
        json_data = json.load(f)
        for item in json_data:
            added_date = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S') if item.get('added', '').strip() else datetime(1900, 1, 1, 0, 0)
            published_date = datetime.strptime(item['published'], '%B, %d %Y %H:%M:%S') if item.get('published', '').strip() else datetime(1900, 1, 1, 0, 0)
            model_instance = DataItem(
                end_year=int(item['end_year']) if item.get('end_year', '') else 0,  
                intensity=int(item['intensity']) if item.get('intensity', '') else 0, 
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'][:255],
                region=item['region'],
                start_year=int(item['start_year']) if item.get('start_year', '') else 0,  
                impact=int(item['impact']) if item.get('impact', '') else 0,  
                added=added_date,
                published=published_date,
                country=item['country'],
                relevance=int(item['relevance']) if isinstance(item.get('relevance', ''), str) and item.get('relevance', '') else 0,  
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'][:255],
                likelihood=int(item['likelihood']) if isinstance(item.get('likelihood', ''), str) and item.get('likelihood', '').strip() else 0  
                
            )
            model_instance.save()

# load_json_data_into_model()