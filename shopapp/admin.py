from django.contrib import admin
from .models import Address, PaymentDetails, Order, Wishlist, Recommendation, OrderItem, JewelryItem

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'line1', 'line2', 'city', 'state', 'postal_code', 'country')

class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expiry_date', 'cvv')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'tracking_number')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name')

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommended_item')

# Custom admin class for JewelryItem
class JewelryItemAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('name', 'price', 'category', 'sku', 'stock_level', 'size', 'ring_size', 'colour', 'material', 'date_created')

    # Filters for the right sidebar
    list_filter = ('category', 'size', 'ring_size', 'material')

    # Fields that can be searched
    search_fields = ('name', 'description', 'category', 'sku')

    # Group fields into sections
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category', 'sku', 'stock_level', 'size', 'ring_size', 'colour', 'material', 'stone', 'stone_size', 'image')
        }),
        ('SEO Information', {
            'fields': ('seo_meta_title', 'seo_meta_description')
        }),
    )

    # Add custom actions
    actions = ['mark_as_out_of_stock']

    # Custom action to mark selected items as out of stock
    def mark_as_out_of_stock(self, request, queryset):
        queryset.update(stock_level=0)
        self.message_user(request, "Selected products marked as out of stock.")
    mark_as_out_of_stock.short_description = "Mark selected products as out of stock"

# Register the models with the custom admin classes
admin.site.register(Address, AddressAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(JewelryItem, JewelryItemAdmin)
