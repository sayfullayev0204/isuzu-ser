from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Mahsulotlar(TranslatableModel):
    categories = (
        ('avtobuslar', 'avtobuslar'),
        ('yuk_mashinalari', 'yuk_mashinalari'),
        ('maxsus_mashinalari', 'maxsus_mashinalari'),
    )
    turi = models.CharField(max_length=200, choices=categories)
    translations = TranslatedFields(
        nomi = models.CharField(max_length=200),
    )
    narxi = models.IntegerField()
    rasm = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Asosiy rasm")


class Image(models.Model):
    product = models.ForeignKey(Mahsulotlar, related_name='images', on_delete=models.CASCADE, verbose_name="Mahsulotlar")
    image = models.ImageField(upload_to='images/', verbose_name="Qo'shimcha rasm")

    def __str__(self):
        return f"Image for {self.product.safe_translation_getter('sarlavha', any_language=True) or 'No Title'}"
