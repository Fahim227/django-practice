from django.contrib import admin

# Register your models here.
from cache.models import User
admin.site.register([User])