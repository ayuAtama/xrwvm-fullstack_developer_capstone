from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):  # or admin.StackedInline
    model = CarModel
    extra = 5  # show one empty form by default

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)