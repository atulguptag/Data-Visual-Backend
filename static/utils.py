# utils.py

import json
from .models import DataItem  # Imported DataItem model

def load_json_data_into_model():
    with open('jsondata.json', 'r') as f:
        json_data = json.load(f)
        for item in json_data:
            model_instance = DataItem(
                end_year=item['end_year'],
                intensity=item['intensity'],
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
                relevance=item['relevance'],
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=item['likelihood']
            )
            model_instance.save()

load_json_data_into_model()