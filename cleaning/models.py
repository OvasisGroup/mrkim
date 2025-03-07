from django.db import models

# Create your models here.
class Category(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to='categories')
    image = models.ImageField(null=True, blank=True, upload_to='ategories')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name