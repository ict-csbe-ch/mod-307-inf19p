from django.contrib import admin

# Register your models here.
from cronjob.models import User
from cronjob.models import Address
from cronjob.models import Ort
from cronjob.models import Cronjob

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Ort)
admin.site.register(Cronjob)