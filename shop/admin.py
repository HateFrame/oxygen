from django.contrib import admin
from .models import User, Product, RequestList

admin.site.register(User)
admin.site.register(Product)
admin.site.register(RequestList)
# Register your models here.
