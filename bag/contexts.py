from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from personalise.models import Personalise


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', [])

    for values in bag:
        item_id = values['product']
        product = get_object_or_404(Product, pk=item_id)
        price = product.price
        total += values['quantity'] * product.price
        if values['extra_requirements']:
            price += 5
            total += 5

        total += Personalise.EXTRA_COST[values['background']]
        total += Personalise.EXTRA_COST[values['text_color']]

        price += Personalise.EXTRA_COST[values['background']]
        price += Personalise.EXTRA_COST[values['text_color']]

        product_count += values['quantity']
        bag_items.append({
            'price': price,
            'item_id': item_id,
            'quantity': values['quantity'],
            'product': product,
            'background': values['background'],
            'extra_requirements': values['extra_requirements'],
            'text_color': values['text_color'],
            'text_content': values['text_content'],
            'id': values['id'],
        })

    if total < settings.BUNDLE_DISCOUNT_THRESHOLD:
        grand_total = total
    else:
        grand_total = float(total) * 0.8

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'bundle_discount_threshold': settings.BUNDLE_DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        'discount': float(total) - float(grand_total),
    }

    return context
