# Generated by Django 4.1.6 on 2023-02-15 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0003_cart_customer_cartproduct_cart_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartproduct",
            name="cart",
        ),
        migrations.RemoveField(
            model_name="cartproduct",
            name="product",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="CartProduct",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
    ]