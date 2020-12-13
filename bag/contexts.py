from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

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
