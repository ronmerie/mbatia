from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def contact(request):
    return render(request, 'contact.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact  # Import your Contact model

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if any of the required fields is empty before saving
        if not name or not email or not message:
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('contact')  # Redirect back to the contact page

        # Use either create or save, not both
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, 'Details successfully processed and saved.')
        return redirect('home')  # Replace 'index' with the actual name or URL pattern

    return render(request, 'contact.html')


