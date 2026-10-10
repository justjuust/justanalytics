import logging

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


def animacel_view(request):
    return render(request, 'animacel.html', )


def veterinary_view(request):
    return render(request, 'veterinary.html', )


def contact_view(request):
    if request.method != 'POST':
        return redirect(reverse('home') + '#tf-contact')

    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, 'index.html', {'form': form})

    email = form.cleaned_data['email']
    message = form.cleaned_data['message']

    # Gmail only sends from the authenticated account, so the visitor's
    # address goes in Reply-To instead of From.
    mail = EmailMessage('Contact Form Message',
                        f"From: {email}\n\n{message}",
                        settings.DEFAULT_FROM_EMAIL,
                        ['just.bajzelj@gmail.com'],
                        reply_to=[email])
    try:
        mail.send(fail_silently=False)
    except Exception:
        logger.exception("Failed to send contact form email")
        messages.error(request, "Sorry, your message could not be sent. "
                                "Please email us directly at just.bajzelj@gmail.com.")
    else:
        messages.success(request, "Thank you! Your message has been sent.")

    return redirect(reverse('home') + '#tf-contact')


class StaticViewSitemap(Sitemap):
    priority = 0.5  # Importance of the URL (1.0 = highest, 0.0 = lowest)
    changefreq = "weekly"  # How frequently the page changes

    def items(self):
        # Return a list of view names or model instances
        return ["home", "case_study_animacel", 'veterinary']

    def location(self, item):
        # Return the URL of the view
        return reverse(item)