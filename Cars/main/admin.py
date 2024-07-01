from django.contrib import admin
from main.models import Car, CarImage

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "make", "model", "yearMfct", "price", "locallyAvailable",)
    inlines = [CarImageInline]

class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car_name", "car_make", "car_model", "image",)

    def car_name(self, obj):
        return obj.car.name

    def car_make(self, obj):
        return obj.car.make

    def car_model(self, obj):
        return obj.car.model

admin.site.register(Car, CarAdmin)
admin.site.register(CarImage, CarImageAdmin)
