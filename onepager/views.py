from django.shortcuts import render
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
# Create your views here.


def index(request):
    return render(request, 'index.html')


def animacel_view(request):
    return render(request, 'animacel.html', )


def veterinary_view(request):
    return render(request, 'veterinary.html', )


class StaticViewSitemap(Sitemap):
    priority = 0.5  # Importance of the URL (1.0 = highest, 0.0 = lowest)
    changefreq = "weekly"  # How frequently the page changes

    def items(self):
        # Return a list of view names or model instances
        return ["home", "case_study_animacel", 'veterinary']

    def location(self, item):
        # Return the URL of the view
        return reverse(item)