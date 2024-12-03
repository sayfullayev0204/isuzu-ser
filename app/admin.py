from django.contrib import admin
from .models import Mahsulotlar,Image,Turi
from parler.admin import TranslatableAdmin


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Mahsulotlar)
class YangiliklarAdmin(TranslatableAdmin):
    inlines = [ImageInline]
    list_display = ('turi', 'nomi')

@admin.register(Turi)
class TurAdmin(TranslatableAdmin):
    list_display = ['nomi']