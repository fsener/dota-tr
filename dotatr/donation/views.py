from django.shortcuts import render
import json, base64, requests, urlparse
from donation.models import DonationTarget
import datetime

pdt_hash = "9Le9iJBWqevVdfaOUAx3XT3kDHrGXUnNmzcABlkJKNqIxHKCt_xTj9uho7G"

def donate_page(request):
	custom_value = {'user':"erkan", 'game':"dota2"} 
	custom_json = json.dumps(custom_value);
	custom_obfuscated = base64.standard_b64encode(custom_json)

	donationTarget = DonationTarget.objects.get(month=datetime.date.today().month)

	return render(request, 'donation/donation_page.html', {'target': donationTarget,'custom': custom_obfuscated, 'o':"sometext"})

def donate_page_success(request):
	pdt = getPDT(request)

	custom = None

	if(pdt['result'] == "SUCCESS"):
		custom = json.loads(base64.standard_b64decode(pdt['custom']))

	donationTarget = DonationTarget.objects.get(month=datetime.date.today().month)
	donationTarget.current += float(pdt['mc_gross'])
	donationTarget.save()

	return render(request, 'donation/donation_page_success.html', {'target': donationTarget, 'response': pdt, 'custom': custom})


def parsePDT(pdt):
	pdts = pdt.split('\n')
	result = pdts.pop(0)
	resultPDT = urlparse.parse_qs("&".join(pdts))

	for key in resultPDT:
		resultPDT[key] = resultPDT[key][0]

	resultPDT['result'] = result

	return resultPDT

def getPDT(req):
	getObj = dict(req.GET.iterlists())
	payload = {'cmd':"_notify-synch", 'tx':getObj[u'tx'], 'at': pdt_hash}
	response = requests.get('https://www.sandbox.paypal.com/cgi-bin/webscr', params=payload)
	pdt = parsePDT(response.content)

	return pdt	