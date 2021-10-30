from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from ..managers import CategoryManager


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('name',)

    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, editable=False)
    # slug = AutoSlugField(populate_from=['name'], allow_unicode=True, unique=True)

    objects = CategoryManager()

    # def slug(self):
    #     return slugify(self.name)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("category_detail", kwargs={"id": self.id})
        # return reverse("category_filter", args=[self.slug,])
        return reverse("cart:category_filter", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}".format(self.name)
