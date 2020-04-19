from django.contrib import admin
from .models import Plate, Tag


# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
    )
