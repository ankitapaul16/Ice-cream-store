from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
context ={
        "variable1":"Ankita is great",
        "variable2":"Adrika is great"
    }
def index(request):
     #context ={
     #  "variable":"This is sent"
     #}
     
     return render (request,'index.html', context)
     #return render(request, 'index.html')
     #return HttpResponse ("This is Home Page.")
def about(request):
     return render (request,'about.html', context)
     #return HttpResponse ("This is About Page.")
def services(request):
     return render (request,'services.html', context)
     #return HttpResponse ("This is Services Page.")
def contact(request):
     if request.method == "POST":
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          
          phone_number=request.POST.get('phone_number')
          city=request.POST.get('city')
          state=request.POST.get('state')
          zip=request.POST.get('zip')
          address_1=request.POST.get('address_1')
          address_2=request.POST.get('address_2')
          email_address=request.POST.get('email_address')
          password=request.POST.get('password')
          comments=request.POST.get('comments')
          date=request.POST.get('date')
          contact = Contact(first_name=first_name,last_name=last_name, phone_number=phone_number,city=city, state=state, zip=zip, address_1=address_1, address_2=address_2, email_address=email_address, password=password,comments=comments,date =datetime.today())
          contact.save()
          messages.success(request, "Your message has been sent!")
     return render (request,'contact.html', context)
     #return HttpResponse ("This is Contact Page.")