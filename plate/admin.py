from django.contrib import admin
from .models import Plate, Tag, PlateImage


# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class PlateImageInline(admin.TabularInline):
    model = PlateImage

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
    )
    inlines = [PlateImageInline]