from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

# Create your models here.

class UserPermited(models.Model):

    username = models.CharField(max_length=11,unique=True)

    def __str__(self):
        return self.username

class LDAPUser(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(blank=True, max_length=255)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
