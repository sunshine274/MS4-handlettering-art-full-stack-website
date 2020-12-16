from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    background = request.POST.get('background')
    extra_requirements = request.POST.get('extra_requirements')
    text_color = request.POST.get('text_color')
    text_content = request.POST.get('text_content')
    default_values = {
        'quantity': quantity,
        'background': 'standard',
        'extra_requirements': '',
        'text_color': 'standard',
        'text_content': '',
        }
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id]['quantity'] += quantity
    else:
        bag[item_id] = default_values
        messages.success(request, f'Added {product.name} to your bag')
    bag[item_id]['background'] = background
    bag[item_id]['extra_requirements'] = extra_requirements
    bag[item_id]['text_color'] = text_color
    bag[item_id]['text_content'] = text_content

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)