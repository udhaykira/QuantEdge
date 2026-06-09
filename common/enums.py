from django.db import models

class OrderType(models.TextChoices):
    BUY="BUY","Buy"
    SELL="SELL","Sell"