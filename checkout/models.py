from django.db import models
from shop.models import Product


class Order(models.Model):
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False,
    )
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=200,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )
    address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )
    town_or_city = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )
    county = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )
    eircode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    order_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
        editable=False,
    )

    def __str__(self):
        """
        Unicode representation of the order model
        """

        return self.order_number


class OrderItem(models.Model):
    order_reference = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        editable=False,
    )
    product_name = models.CharField(
        'Product name',
        max_length=50,
        editable=False,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        editable=False,
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        editable=False,
    )

    def __str__(self):
        """
        Unicode representation of the order item model
        """

        return self.order_reference.order_number + ' - ' \
            + self.product_name
