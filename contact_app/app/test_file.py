import pytest    
from app.models import Contact 
from app.views import contact_list_view 
from django.urls import reverse, resolve
from django.test import RequestFactory

@pytest.mark.django_db #give test access to database  
def test_contact_create():    
    # Create dummy data       
    contact = Contact.objects.create(full_name="Shubham Chaurasia", phone_number="75859538350",)    
    # Assert the dummy data saved as expected       
    assert contact.full_name=="Shubham Chaurasia"      
    assert contact.phone_number=="75859538350"

...

@pytest.mark.django_db # 
def test_view():
    path = reverse("contact_list")
    request = RequestFactory().get(path) # get the path for the list of contacts
    response = contact_list_view(request)
    assert response.status_code == 200 # assert status code from requesting the view is 200(OK success status response code)

def test_url():            
    path = reverse('contact_list')
    print(path)     
    assert resolve(path).view_name == "contact_list"