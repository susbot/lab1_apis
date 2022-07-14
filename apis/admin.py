from django.contrib import admin

# Import Models from Project
from apis import models

# Register your models here.


# Register models
admin.site.register(models.UserProfile)
