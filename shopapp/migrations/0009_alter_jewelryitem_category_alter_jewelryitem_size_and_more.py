# Generated by Django 5.0.6 on 2024-08-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0008_jewelryitem_category_jewelryitem_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelryitem',
            name='category',
            field=models.CharField(choices=[('Rings', 'Rings'), ('Earrings', 'Earrings'), ('Necklaces', 'Necklaces'), ('Bracelets', 'Bracelets'), ('Uncategorized', 'Uncategorized')], default='Uncategorized', max_length=50),
        ),
        migrations.AlterField(
            model_name='jewelryitem',
            name='size',
            field=models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='jewelryitem',
            name='stock_level',
            field=models.IntegerField(choices=[(0, 'Out of Stock'), (10, 'Low Stock'), (50, 'In Stock'), (100, 'High Stock')], default=0),
        ),
    ]
