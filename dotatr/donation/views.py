from django.shortcuts import render
import json
import base64
import requests

pdt_hash = "9Le9iJBWqevVdfaOUAx3XT3kDHrGXUnNmzcABlkJKNqIxHKCt_xTj9uho7G"

def donate_page(request):
	custom_value = {'user':"", 'game':"dota2"} 
	custom_json = json.dumps(custom_value);
	custom_obfuscated = base64.standard_b64encode(custom_json)

	return render(request, 'donation/donation_page.html', {'custom': custom_obfuscated, 'o':"sometext"})

def donate_page_success(req):
	payload = {'cmd':"_notify-synch", 'tx':req.GET.tx, 'at': pdt_hash}
	response = requests.get('https://www.sandbox.paypal.com/cgi-bin/webscr', payload)

	print response

	return render(request, 'donation/donation_page_success.html', {'response': response})