from django.http import JsonResponse
from .models import Order


def order_list(request):
    orders = Order.objects.all()
    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "user": o.user.username,
            "total": o.price * o.quantity * 1.1,
        })
    if len(result) > 100:
        result = result[:100]
    return JsonResponse(result, safe=False)
