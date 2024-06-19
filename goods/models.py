from email.mime import image
from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название категории"
    )
    slug = models.SlugField(
        max_length=250, unique=True, blank=True, null=True, verbose_name="URL категории"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Назва товару"
    )
    slug = models.SlugField(
        max_length=250, unique=True, blank=True, null=True, verbose_name="URL товару"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    img = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Зображення"
    )
    price = models.DecimalField(
        default=0.00, max_digits=6, decimal_places=2, verbose_name="Ціна"
    )
    discount = models.DecimalField(
        default=0, max_digits=4, decimal_places=2, verbose_name="Скидка"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категорія"
    )

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ["id"]
        

    def __str__(self):
        return self.name
    
    def show_id(self):
        return f"{self.id:05}"
    
    def end_price(self):
        if self.discount:
            return round(self.price * (1-self.discount/100),2)
        return self.price
