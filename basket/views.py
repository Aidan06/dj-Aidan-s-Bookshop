from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)

    if request.method == 'POST':
        product_id = int(request.POST.get('productid')[0])
        product_qty = int(request.POST.get('productqty')[0])
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

    return JsonResponse({'error': 'Invalid request'})
