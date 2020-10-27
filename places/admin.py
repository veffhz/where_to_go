from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place
from places.models import Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    readonly_fields = ["place_image_preview"]

    def place_image_preview(self, obj):
        url = obj.place_image.url
        return format_html(
            '<img src="{}" width="auto" style="max-height: 200px;" />', url
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ImageInline,
    ]
