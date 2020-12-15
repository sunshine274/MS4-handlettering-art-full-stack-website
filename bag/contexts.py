from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.BUNDLE_DISCOUNT_THRESHOLD:
        grand_total = total
    else:
        grand_total = total * 0.8

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'bundle_discount_threshold': settings.BUNDLE_DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
