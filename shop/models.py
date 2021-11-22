from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Доступен к продаже или аренде")
    all_count = models.IntegerField(default=1, verbose_name="Общее количество")
    remains = models.IntegerField(default=1, verbose_name="Оставшееся количество")
    author = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name="Автор объявления")

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=128, null=True, blank=True, verbose_name="Логин")
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name="Имя")
    phone_number = models.CharField(max_length=12, null=True, blank=True, verbose_name="Номер телефона")

    def __str__(self):
        return self.name


class RequestList(models.Model):
    user = models.CharField(max_length=64, verbose_name="Имя")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    email = models.CharField(max_length=128, verbose_name="Электронная почта")
    comment = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.phone_number
