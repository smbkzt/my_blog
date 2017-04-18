from django.shortcuts import render
from contact.forms import ContactForm


def contact_page(request):
    form = ContactForm()
    context = {
		'form': form
	}
    return render(request, 'blog/contact.html', context)
