from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import PersonalisationForm


def personalise(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    personalisation_form = PersonalisationForm()

    context = {
        'product': product,
        'form': personalisation_form,
    }

    return render(request, 'personalise/personalise.html', context)
