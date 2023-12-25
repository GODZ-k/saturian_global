from django.db import models

# Create your models here.

# category

class Category(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
class product(models.Model):
    categories=models.ForeignKey(Category,null=True,blank=True,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=300,null=True,blank=True)
    image=models.ImageField(upload_to="image",null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
# service card
class service_card(models.Model):
    name=models.CharField(max_length=255 , null=True, blank=True)
    image=models.ImageField(upload_to="image",null=True,blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Service Cards'




class Contact(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    email=models.EmailField(max_length=255,null=True, blank=True)
    contact=models.CharField(null=True, blank=True,max_length=255)
    subject=models.CharField(max_length=255,null=True, blank=True)
    message=models.TextField(null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self)-> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Contact information'


class Product_form(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    email=models.EmailField(max_length=255,null=True, blank=True)
    contact=models.IntegerField(null=True, blank=True)
    period=models.CharField(null=True, blank=True, max_length=255)
    Quantity=models.IntegerField(null=True, blank=True)
    product=models.CharField(max_length=255,null=True, blank=True)
    message=models.TextField(null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self)-> str:
        return self.name

    class Meta:
        verbose_name_plural = 'product enquiry'