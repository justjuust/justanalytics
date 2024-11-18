from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
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

class StaticViewSitemap(Sitemap):
    priority = 0.5  # Importance of the URL (1.0 = highest, 0.0 = lowest)
    changefreq = "weekly"  # How frequently the page changes

    def items(self):
        # Return a list of view names or model instances
        return ["home", "case_study_animacel", 'veterinary', 'contact_view']

    def location(self, item):
        # Return the URL of the view
        return reverse(item)