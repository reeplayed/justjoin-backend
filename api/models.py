from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from .utils import unique_slug_generator

class Location(models.Model):
    lat = models.DecimalField( max_digits=15, decimal_places=8)
    lng = models.DecimalField( max_digits=15, decimal_places=8)
    place_id = models.CharField(max_length=50, null=True)

class Offert(models.Model):
    tech = models.CharField(max_length=12)
    company_name = models.CharField(max_length=100)
    offer_title = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    company_size = models.IntegerField(default=0)
    salary_from = models.IntegerField(default=0)
    salary_to = models.IntegerField(default=0)
    emp_type = models.CharField(max_length=12, null=True)
    place_id = models.CharField(max_length=50, null=True)
    exp_lvl = models.CharField(max_length=12, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    description = models.TextField(default='<p>elo</p>')
    location = models.ForeignKey(Location , related_name='offerts', on_delete=models.CASCADE, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

class Tech(models.Model):
    tech = models.CharField(max_length=100, blank=True, null=True)
    tech_lvl = models.CharField(max_length=100, blank=True, null=True)
    offert = models.ForeignKey( Offert, related_name='technology', on_delete=models.CASCADE, blank=True, null=True)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Offert)