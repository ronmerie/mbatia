from django.urls import path,include
from .views import index
from backend.views import contact
from backend.views import views

urlpatterns = [
    path('', index, name='index'), 
    path('contact/', contact, name='contact'),
    ]