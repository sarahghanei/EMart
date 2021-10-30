from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from ..managers import BrandManager
from django_extensions.db.fields import AutoSlugField


class Brand(models.Model):
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
        ordering = ('name',)

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, editable=False)
    # slug = AutoSlugField(populate_from=['name'], allow_unicode=True, unique=True)
    objects = BrandManager()

    # def slug(self):
    #     return slugify(self.name)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Brand, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("brand_detail", kwargs={"id": self.id})
        return reverse("brand_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}".format(self.name)
