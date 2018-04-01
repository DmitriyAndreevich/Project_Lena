from django.db import models
from django.utils import timezone



class Projects (models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(max_length=75, blank=True)
	is_active = models.BooleanField(default=True)



class Posts(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(max_length=75, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=255)
    message = models.TextField()
