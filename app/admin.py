from django.contrib import admin
from .models import Mahsulotlar,Image
from parler.admin import TranslatableAdmin


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Mahsulotlar)
class YangiliklarAdmin(TranslatableAdmin):
    inlines = [ImageInline]
    list_display = ('turi', 'nomi')