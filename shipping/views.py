from django.shortcuts import render
from django.core.mail import send_mail
from  django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'shipping/index.html')

def about(request):
    return render(request, 'shipping/about.html')

def service(request):
    return render(request, 'shipping/service.html')

def products(request):
    return render(request, 'shipping/products.html')

# def contact(request):
#     return render(request, 'shipping/contact.html')

def howtobuy(request):
    return render(request, 'shipping/howtobuy.html')

def shop(request):
    return render(request, 'shipping/shop.html')

def contact(request):
	if request.method=='POST':
		message_name = request.POST.get('message-name')
		message_email = request.POST.get('message-email')
		message_phone = request.POST.get('message-phone')
		message = request.POST.get('message')
                

		# Send an emai
		send_mail(message_name,message, message_email,['mistourasal@gmail.com'])

		#send_mail(message_name,message, message_email,['saleemkhattak333@gmail.com'])

		return render(request, 'shipping/contact.html', {'message_name': message_name})
	else:
                return render(request,'shipping/contact.html')
