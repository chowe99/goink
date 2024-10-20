from django.shortcuts import render

from django.http import HttpResponse
from .scraper import scrape_data_gov, scrape_worldbank
import requests

def scrape_view(request):
    # Scrape datasets from both sources
    scrape_data_gov()
    scrape_worldbank()
    
    return HttpResponse("Scraping from data.gov and data.worldbank.org is complete!")

# scraper/views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class AirQualityDataAPIView(APIView):
    def get(self, request):
        url = "https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.json?accessType=DOWNLOAD"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Process the data to extract relevant fields
            processed_data = self.process_data(data)

            return Response(processed_data)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=500)

    def process_data(self, data):
        columns = data['meta']['view']['columns']
	    data_rows = data['data']
        # Build a mapping from column name to index
	    column_map = {column['name']: idx for idx, column in enumerate(columns)}
	    # Define the fields to extract
	    target_fields = ['Date', 'Pollution Level']  # Adjust based on actual column names
	    # Find indices for the target fields
	    field_indices = {field: column_map[field] for field in target_fields if field in column_map}
	    # Extract and process data
	    processed = []
	    for row in data_rows:
	        entry = {}
	        for field, idx in field_indices.items():
	            entry[field] = row[idx]
	        # Convert Pollution Level to float, if applicable
	        if 'Pollution Level' in entry:
	            try:
	                entry['Pollution Level'] = float(entry['Pollution Level'])
	            except (ValueError, TypeError):
	                entry['Pollution Level'] = None
	        processed.append(entry)
	    return processed
# Create your views here.

