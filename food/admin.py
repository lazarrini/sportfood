from django.contrib import admin
from .models import *

class GoodInOrderInline(admin.TabularInline):
    model = GoodInOrder
    extra = 0

class GoodImageInline(admin.TabularInline):
    model = GoodImage
    extra = 0



class GoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Good._meta.fields]
    inlines = [GoodImageInline]

    class Meta:
        model = Good

admin.site.register(Good, GoodAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class PointOfDeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PointOfDelivery._meta.fields]

    class Meta:
        model = PointOfDelivery


admin.site.register(PointOfDelivery, PointOfDeliveryAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [GoodInOrderInline]
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class GoodInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GoodInOrder._meta.fields]

    class Meta:
        model = GoodInOrder


admin.site.register(GoodInOrder, GoodInOrderAdmin)

class GoodImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GoodImage._meta.fields]

    class Meta:
        model = GoodImage


admin.site.register(GoodImage, GoodImageAdmin)