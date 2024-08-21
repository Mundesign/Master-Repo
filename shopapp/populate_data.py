from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from your_app.models import Address, PaymentDetails, Order, Wishlist, Recommendation, OrderItem
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with duplicate data for testing purposes'

    def handle(self, *args, **kwargs):
        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'testuser@example.com', 'password': 'password'})
        
        # Create duplicate addresses
        for _ in range(5):
            Address.objects.create(user=user, address='123 Test Street')

        # Create duplicate payment details
        for _ in range(5):
            PaymentDetails.objects.create(user=user, card_number='1234567812345678', expiry_date=date(2025, 12, 31), cvv='123')

        # Create duplicate orders
        for _ in range(5):
            order = Order.objects.create(user=user, tracking_number='TRACK123456')
            # Create duplicate order items for each order
            for _ in range(3):
                OrderItem.objects.create(order=order, product_name='Test Product', quantity=1)

        # Create duplicate wishlist items
        for _ in range(5):
            Wishlist.objects.create(user=user, item_name='Test Item')

        # Create duplicate recommendations
        for _ in range(5):
            Recommendation.objects.create(user=user, recommended_item='Recommended Item')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with duplicate data'))
