import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mundesign.settings')
django.setup()

from django.contrib.auth.models import User
from shopapp.models import Address, PaymentDetails, Order, Wishlist, Recommendation, OrderItem

# Use the existing superuser
user = User.objects.get(username='mundesign123')  

# Create Address instance
address = Address.objects.create(
    user=user,
    line1='123 Test Line 1',
    line2='Apt 1',
    city='Test City',
    state='Test State',
    postal_code='12345',
    country='Test Country'
)

# Create PaymentDetails instance with the correct date format
payment_details = PaymentDetails.objects.create(
    user=user,
    card_number='1234567890123456',
    expiry_date=date(2025, 12, 1),  # Setting a default day (1st of the month)
    cvv=123
)

# Create Order instance
order = Order.objects.create(
    user=user,
    tracking_number='TRACK123456'
)

# Create OrderItem instance
order_item = OrderItem.objects.create(
    order=order,
    product_name='Test Product',
    quantity=1
)

# Create Wishlist instance
wishlist = Wishlist.objects.create(
    user=user,
    item_name='Test Item'
)

# Create Recommendation instance
recommendation = Recommendation.objects.create(
    user=user,
    recommended_item='Recommended Product'
)

# Print created instances
print(Address.objects.filter(user=user))
print(PaymentDetails.objects.filter(user=user))
print(Order.objects.filter(user=user))
print(OrderItem.objects.filter(order=order))
print(Wishlist.objects.filter(user=user))
print(Recommendation.objects.filter(user=user))
