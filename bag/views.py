from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from personalise.models import Personalise


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    sub_total = product.price

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    background = request.POST.get('background')
    extra_requirements = request.POST.get('extra_requirements')
    text_color = request.POST.get('text_color')
    text_content = request.POST.get('text_content')
    bag = request.session.get('bag', [])
    if extra_requirements:
        sub_total += 5

    sub_total += Personalise.EXTRA_COST[background]
    sub_total += Personalise.EXTRA_COST[text_color]
    default_values = {
        'product': product.id,
        'sub_total': float(sub_total),
        'quantity': quantity,
        'background': background,
        'extra_requirements': extra_requirements,
        'text_color': text_color,
        'text_content': text_content,
        'id': len(bag) + 1,
        }
    bag.append(default_values)
    messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', [])
        removed_item = None
        new_bag = []

        for item in bag:
            if item['id'] == int(item_id):
                removed_item = item
                continue
            new_bag.append(item)

        request.session['bag'] = new_bag
        if removed_item:
            product = Product.objects.get(id=removed_item['product'])
            messages.success(request, f'Removed {product.name} from your bag')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing product {e}')
        return HttpResponse(status=500)
