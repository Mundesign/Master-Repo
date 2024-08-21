from django import forms
from .models import JewelryItem

class JewelryItemForm(forms.ModelForm):
    class Meta:
        model = JewelryItem
        fields = [
            'name', 'description', 'price', 'category', 'sku', 'stock_level',
            'size', 'ring_size', 'colour', 'material', 'stone', 'stone_size',
            'image', 'seo_meta_title', 'seo_meta_description'
        ]
