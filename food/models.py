from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Good(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    calorie_content = models.PositiveIntegerField()
    #image = models.ImageField(upload_to='goods_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Товар %s" % self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class GoodImage(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='goods_images/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Фотография %s" % self.id

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

class Status(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"



class PointOfDelivery(models.Model):
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Пункт выдачи %s" % self.name

    class Meta:
        verbose_name = "Пункт выдачи"
        verbose_name_plural = "Пункты выдачи"

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)
    customer_address = models.EmailField(blank=True, null=True, default=None)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class GoodInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    price_per_good = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.good.name

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        price_per_good = self.good.price
        self.price_per_good = price_per_good
        self.total_price = self.quantity*price_per_good

        super(GoodInOrder, self).save(*args, **kwargs)

def good_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_goods_in_order = GoodInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_goods_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(good_in_order_post_save, sender = GoodInOrder)

