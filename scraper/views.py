from django.shortcuts import render

from django.http import HttpResponse
from .scraper import scrape_data_gov, scrape_worldbank

def scrape_view(request):
    # Scrape datasets from both sources
    scrape_data_gov()
    scrape_worldbank()
    
    return HttpResponse("Scraping from data.gov and data.worldbank.org is complete!")

# Create your views here.

