from django.views.generic import DeleteView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import AddLinkForm
from .models import Link


"""
For our home view we need to pass to the template:
- qs (queryset)
- number of items
- number of items discounted
- form
- error (if exists)

For our Update and Delete of our Amazon Items:
- Update View
- Delete View
"""


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


def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')


class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/confirm_del.html'
    success_url = reverse_lazy('home')

