from django.shortcuts import render
import json
import base64
import requests

def donate_page(request):
	custom_value = {'user':"", 'game':"dota2"} 
	custom_json = json.dumps(custom_value);
	custom_obfuscated = base64.standard_b64encode(custom_json)

	return render(request, 'donation/donation_page.html', {'custom': custom_obfuscated, 'o':"sometext"})

def donate_page_success(request):
	return render(request, 'donation/donation_page_success.html', {'tx': request.GET.tx,})