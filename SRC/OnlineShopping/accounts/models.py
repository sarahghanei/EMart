from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from .managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    """
        Customized user, which can have 3 roles :
        admin
        staff
        customer
    """

    class Meta:
        verbose_name = 'کاربر کلی'
        verbose_name_plural = 'کاربران کلی'

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Unknown'),
    )

    # we want email attribute to be unique and we want to use it as unique identifier
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to='accounts/static/accounts/avatars/', null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER_CHOICES, max_length=8)
    last_login = models.DateTimeField(auto_now=True)
    dob = models.DateField(default=None, blank=True, null=True)
    # create slug based on unique username
    slug = AutoSlugField(populate_from=['first_name', 'last_name'], unique=True)
    objects = CustomUserManager()
    # unique identifier
    USERNAME_FIELD = 'email'
    # required fields for creating superuser
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"slug": self.slug})

    def has_perm(self, perm, obj=None):
        # for checking specific permission
        # by default True
        return True

    def has_module_perms(self, app_label):
        # access to models of the given app
        # by default True
        return True

    def __str__(self):
        return self.get_full_name()


class Customer(CustomUser):
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
        proxy = True

    is_superuser = False
    is_staff = False
    is_active = True


class Admin(CustomUser):
    class Meta:
        verbose_name = 'مدیر'
        verbose_name_plural = 'مدیران'
        proxy = True

    is_superuser = True
    is_staff = True
    is_active = True


class Staff(CustomUser):
    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'
        proxy = True

    is_superuser = False
    is_staff = True
    is_active = True


class Address(models.Model):
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    detail = models.TextField(max_length=2000)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    # one of the addresses should be the default address
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return "{} address:{}-{}-{}-{}".format(self.owner, self.country, self.province, self.street, self.postal_code)
