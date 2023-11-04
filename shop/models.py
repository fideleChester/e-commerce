from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_added"] #Le premier créer sera affiché
        verbose_name_plural = "catégories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="categorie")
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_added"]
        verbose_name_plural = "produits"

    def __str__(self):
        return self.title
