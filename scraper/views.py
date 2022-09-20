from django.shortcuts import render


# Create your views here.
def amazon_scraped_items(request):
    return render(request, "base.html")