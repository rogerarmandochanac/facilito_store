from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField()
    create_att = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


def set_slug(sender, instance, *a, **k):
    instance.slug = slugify(instance.title)
    

pre_save.connect(set_slug, sender=Product)