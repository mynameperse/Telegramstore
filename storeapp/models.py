from django.db import models
from django.urls import reverse

# Models of categories
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('storeapp:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    price = models.IntegerField(default=0)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='uploads/pimages')
    image2 = models.ImageField(upload_to='uploads/pimages')
    image3 = models.ImageField(upload_to='uploads/pimages')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('storeapp:product_detail', args=[self.id])
