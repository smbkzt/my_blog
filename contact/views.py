from django.shortcuts import render
from django.contrib import messages
from .models import Contact


def contact_page(request):
    if request.method == "GET":
        return render(request, 'contact/contact.html')
    else:
        contact_data = Contact(
            fullname=request.POST['fullname'],
            email=request.POST['email'],
            text=request.POST['text'])
        contact_data.save()
        messages.success(request, "Thank you! Your feedback has been sent.")
        return render(request, 'contact/contact.html')
