from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request. "There's nothing here yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
