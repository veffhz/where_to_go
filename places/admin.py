from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place
from places.models import Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.file:
            url = obj.file.url
            return format_html(
                '<img src="{}" width="auto" style="max-height: 200px;" />', url
            )
        else:
            return 'Здесь будет превью, когда вы выберете файл'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ImageInline,
    ]
