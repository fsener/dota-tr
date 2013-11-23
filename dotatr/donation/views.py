from django.shortcuts import render
from pprint import pprint

def donate_page(request):
	return render(request, 'donation/donation_page.html', {})

def donate_page_success(request):
	#burda bilgiler gelicek
	
	pprint (vars(request))
	return render(request, 'donation/donate_page_success.html', {})