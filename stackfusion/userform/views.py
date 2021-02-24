from django.shortcuts import render,redirect
from django.contrib import messages
from .models import form
#for sendding mail
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        phone=request.POST['phone_no']
        if len(str(phone))==10:
            user=form(name=name,dob=dob,email=email,phone=phone)
            user.save()
            to=email
            context={
            'name':name,
            'email':email,
            'dob':dob,
            'phone':phone,
                }
            html_content =render_to_string("email.html",context)
            text_content=strip_tags(html_content)
            emaiil=EmailMultiAlternatives(

                "Your Form submission",  #subject
                text_content, #email containt
                settings.EMAIL_HOST_USER, #from Email
                to=[request.POST['email']],    #add list of Recipents Here
            )
            emaiil.attach_alternative(html_content,"text/html")
            emaiil.send()
            return redirect('details')

        else:
            messages.info(request,"Please enter A Valid Phone no!")
            return redirect('index')

    return render(request,'index.html')

def details(request):
    data=form.objects.all()
    return render(request,'details.html',{'data':data } )

