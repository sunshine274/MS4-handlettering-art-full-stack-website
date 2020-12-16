from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing here yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HwG20ASaZPrwd1o54Pvx9kO9bpAJs6Sp0uDqOtva6rBa6ZvC4dIETNdeEyd80yuiuuxSqweVKTUUAHhqwIt8IQV00HO5c61Ev',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
