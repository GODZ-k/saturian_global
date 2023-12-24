from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(service_card)

admin.site.register(Category)


admin.site.register(product)

class show_contact(admin.ModelAdmin):
   list_display=["name","email","contact","subject","message","time"]
admin.site.register(Contact,show_contact)



class product_enquiry(admin.ModelAdmin):
    list_display=["name","email","contact","period","Quantity","product","message","time"]


admin.site.register(Product_form,product_enquiry)