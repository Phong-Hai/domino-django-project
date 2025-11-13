from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .. models import User, Invoice, InvoiceItem, Product


def process_checkout(request):
    return render(request, "pages/invoice.html")


@require_http_methods(["POST"])
@csrf_exempt  # Remove this in production and use proper CSRF token
def create_invoice(request):
    try:
        data = json.loads(request.body)
        cart_items = data.get('cart', [])

        if not cart_items:
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        # Create new invoice
        invoice = Invoice.objects.create()

        # Create invoice items
        for item in cart_items:
            try:
                product = Product.objects.get(id=item['id'])
                InvoiceItem.objects.create(
                    invoice=invoice,
                    product=product,
                    quantity=item['quantity'],
                    price=item['price']
                )
            except Product.DoesNotExist:
                # Handle missing product
                invoice.delete()
                return JsonResponse(
                    {'error': f"Product {item['id']} not found"},
                    status=404
                )

        return JsonResponse({
            'success': True,
            'invoice_id': invoice.id,
            'message': 'Order placed successfully!'
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)