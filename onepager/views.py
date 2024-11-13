from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.


def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


def animacel_view(request):
    return render(request, 'animacel.html', )


def veterinary_view(request):
    return render(request, 'veterinary.html', )


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail('Contact Form Message',
                      email + "\n" + message, email,
                      ['just.bajzelj@gmail.com'],
                      fail_silently=False)
            # Optionally, redirect or render a success page
    else:
        form = ContactForm()

    return render(request, 'index.html',
                  {'form': form})