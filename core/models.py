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