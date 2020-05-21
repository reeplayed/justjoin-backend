from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from .utils import unique_slug_generator, random_image

class Location(models.Model):
    lat = models.DecimalField( max_digits=15, decimal_places=8)
    lng = models.DecimalField( max_digits=15, decimal_places=8)
    place_id = models.CharField(max_length=50)

class Offert(models.Model):
    tech = models.CharField(max_length=12)
    company_name = models.CharField(max_length=100)
    offer_title = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    company_size = models.IntegerField(default=0)
    salary_from = models.IntegerField(default=0)
    salary_to = models.IntegerField(default=0)
    emp_type = models.CharField(max_length=12)
    place_id = models.CharField(max_length=50)
    exp_lvl = models.CharField(max_length=12)
    image = models.ImageField(default=random_image())
    description = models.TextField(default='<p>elo</p>', null=True, blank=True)
    location = models.ForeignKey(Location , related_name='offerts', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

class Tech(models.Model):
    tech = models.CharField(max_length=100)
    tech_lvl = models.CharField(max_length=100)
    offert = models.ForeignKey( Offert, related_name='technology', on_delete=models.CASCADE)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Offert)