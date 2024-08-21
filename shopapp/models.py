from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.line1}, {self.city}, {self.state}, {self.country}'

class PaymentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=50)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_item = models.CharField(max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()

class JewelryItem(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    CATEGORY_CHOICES = [
        ('Rings', 'Rings'),
        ('Earrings', 'Earrings'),
        ('Necklaces', 'Necklaces'),
        ('Bracelets', 'Bracelets'),
        ('Uncategorized', 'Uncategorized'),
    ]

    STOCK_LEVEL_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
    ] + [(str(i), str(i)) for i in range(1, 21)]  # Adding 1 to 20 as choices

    stock_level = models.CharField(
        max_length=15,
        choices=STOCK_LEVEL_CHOICES,
        default='out_of_stock',
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='jewelry_images/')
    date_created = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Uncategorized')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=50, unique=True, default="SKU0000")
    stock_level = models.IntegerField(choices=STOCK_LEVEL_CHOICES, default=0)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    ring_size = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    colour = models.CharField(max_length=50, default="Unknown")
    material = models.CharField(max_length=100, default="Unknown")
    stone = models.CharField(max_length=100, blank=True, null=True)
    stone_size = models.CharField(max_length=50, blank=True, null=True)
    seo_meta_title = models.CharField(max_length=70, blank=True, null=True)
    seo_meta_description = models.CharField(max_length=160, blank=True, null=True)  # Corrected this line

    def __str__(self):
        return self.name
