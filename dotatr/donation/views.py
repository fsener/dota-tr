from django.shortcuts import render

def donate_page(request):
	return render(request, 'donation/donation_page.html', {})

def donate_page_success(request):
	#burda bilgiler gelicek
	return render(request, 'donation/donation_page_success.html', {})