from django.shortcuts import render

from .forms import AddLinkForm
from .models import Link

"""
For our home view we need to pass to the template:
- qs (queryset)
- number of items
- number of items discounted
- form
- error (if exists)
"""


# Create your views here.
# def amazon_scraped_items(request):
#     return render(request, "base.html")


def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "ERROR. Cannot able to get the name or price."
        except:
            error = "An unexpected error has occured."
        
    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = []
        for item in qs:
            if (item.new_price < item.current_price) and (item.new_price != 0):
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error
    }

    return render(request, 'links/main.html', context)

