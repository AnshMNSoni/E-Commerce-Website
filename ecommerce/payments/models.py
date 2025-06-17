from django.db import models

from django.db import models
from orders.models import Order

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('COD', 'Cash on Delivery'),
        ('Card', 'Credit/Debit Card'),
        ('UPI', 'UPI'),
        ('NetBanking', 'Net Banking'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Success')
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.pk}"
