from django.shortcuts import render
from .models import Contact

def contact_list_view(request):
    contact = Contact.objects.all()
    return render(request, "app/contact_list.html", {'contact':contact})