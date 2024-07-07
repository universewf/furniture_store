from django.db import models

# Create your models here.
# null-поле не имеет значения
# blank - поле может быть пустым


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")


    class Meta:
        db_table = "category" #как отображать модель в БД
        verbose_name = "Категорию" #название категории в ед.числе
        verbose_name_plural = "Категории" #название категории в мн.числе

    def __str__(self):
        return self.name #отображение названия queryseta




class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(to=Categories,on_delete=models.CASCADE,verbose_name="Категория")


    class Meta:
        db_table = "product"  ##как отображать модель в БД
        verbose_name = "Продукт" #название категории в ед.числе
        verbose_name_plural = "Продукты" #название категории в мн.числе

    def __str__(self):
        return self.name #отображение названия queryseta
