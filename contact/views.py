from django.shortcuts import render
from django.contrib import messages
from contact.forms import ContactForm
from .models import Contact


def contact_page(request):
    if request.method == "GET":
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'blog/contact.html', context)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            fullname = request.POST['fullname']
            text_field = request.POST['text']
            contact_data_form = Contact(
                fullname=fullname, email=email, text=text_field)
            contact_data_form.save()
            messages.success(
                request, "Thank you! Your feedback has been sent.")

        return render(request, 'blog/contact.html')
