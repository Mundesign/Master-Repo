from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Order, Address, PaymentDetails, Wishlist, Recommendation, OrderItem, JewelryItem
from .forms import JewelryItemForm
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def home(request):
    return render(request, 'home.html')

def demo(request):
    return render(request, 'demo.html')

def explore_more(request):
    return render(request, 'explore_more.html')

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password"
    return render(request, 'login.html', {'error': error})

def logged_out(request):
    return render(request, 'logged_out.html')

@login_required
def my_account(request):
    return render(request, 'my_account.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def order_history_json(request):
    orders = [
        {
            "order_id": 1,
            "order_date": "2024-06-01",
            "items_purchased": "Item A, Item B",
            "total_amount": 100,
            "order_status": "Delivered",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-05"
        },
        {
            "order_id": 2,
            "order_date": "2024-06-02",
            "items_purchased": "Item C, Item D",
            "total_amount": 90,
            "order_status": "In Transit",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-10"
        },
        {
            "order_id": 3,
            "order_date": "2024-06-10",
            "items_purchased": "Item E, Item F",
            "total_amount": 150,
            "order_status": "Not Delivered",
            "delivery_address": "123 Street, City",
            "delivery_date": "2024-06-15"
        },
    ]
    return JsonResponse(orders, safe=False)

@login_required
def saved_addresses(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'saved_addresses.html', {'addresses': addresses})

@login_required
def saved_payment_details(request):
    payment_details = PaymentDetails.objects.filter(user=request.user)
    return render(request, 'saved_payment_details.html', {'payment_details': payment_details})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def recommendations(request):
    recommendations = Recommendation.objects.filter(user=request.user)
    return render(request, 'recommendations.html', {'recommendations': recommendations})

@login_required
def individual_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'individual_order.html', {'order': order, 'order_items': order_items})

@login_required
def return_order(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        order.status = 'Returned'
        order.save()
        return redirect('order_history')
    return render(request, 'return_order.html')

@login_required
def add_jewelry_item(request):
    if request.method == 'POST':
        form = JewelryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jewelry_list')
    else:
        form = JewelryItemForm()
    return render(request, 'add_jewelry_item.html', {'form': form})

def jewelry_list(request):
    jewelry_items = JewelryItem.objects.all().order_by('-date_created')
    paginator = Paginator(jewelry_items, 3)  # Show 3 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jewelry_list.html', {'page_obj': page_obj})

# Add the cart-related views

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        cart[item_id]['quantity'] += 1
    else:
        cart[item_id] = {'quantity': 1}
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    for item_id, item_data in cart.items():
        item = get_object_or_404(add_jewelry_item, id=item_id)
        items.append({
            'item': item,
            'quantity': item_data['quantity'],
        })
    return render(request, 'cart_detail.html', {'items': items})

def update_cart(request, item_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart[item_id]['quantity'] = quantity
    else:
        del cart[item_id]
    request.session['cart'] = cart
    return redirect('cart_detail')
