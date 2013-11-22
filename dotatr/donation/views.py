from django.shortcuts import render

def donate_page(request):
	return render(request, 'donation/donation_page.html', {})