from django.contrib import admin

from .models import Osinfo
from .models import Maker
from .models import PModel
from .models import Product
from .models import PPhoto

# Register your models here.

admin.site.register(Osinfo)
admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(Product)
admin.site.register(PPhoto)
