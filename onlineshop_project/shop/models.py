from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
#SEO 작업 : 검색이 잘 되게 하기 위한 작업

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    meta_description = models.CharField(max_length=250, blank=True)  #검색엔진이 읽어가는 글자 수 제한

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ""


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    meta_description = models.CharField(max_length=250, blank=True)  # 검색엔진이 읽어가는 글자 수 제한


    image = models.ImageField(upload_to='product/%Y/%m/%d')
    description = RichTextUploadingField(blank=True)

    price = models.IntegerField()
    stock = models.IntegerField()
    #PositiveIntegerField() = 우리는 창고제고랑 연동시키지 않겠다
    available_display = models.BooleanField(default=True)
    available_order = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ""


