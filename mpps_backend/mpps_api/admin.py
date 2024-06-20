from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BusinessLicense)
admin.site.register(TransitPass)
admin.site.register(Payment)
admin.site.register(Transaction)