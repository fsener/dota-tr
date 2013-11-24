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
	getObj = dict(req.GET.iterlists())
	print getObj

	payload = {'cmd':"_notify-synch", 'tx':getObj[u'tx'], 'at': pdt_hash}
	response = requests.get('https://www.sandbox.paypal.com/cgi-bin/webscr', params=payload)

	print response.custom

	return render(req, 'donation/donation_page_success.html', {'response': response})