from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings


class Channel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=50)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None)

    def rating_num(self):
        ratings = Rate.objects.filter(course=self)
        return len(ratings)
    
    def avg_rating(self):
        ratings = Rate.objects.filter(course=self)
        sum = 0
        for rate in ratings:
            stars = int(rate.stars)
            sum += stars
        ratings_num = len(ratings)
        if ratings_num == 0:
            return 0
        return sum/ratings_num



    def __str__(self):
        return self.title
    

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title
    
    class Meta:
        unique_together = (('user', 'course'),) # user can't rate the same meal for many times
        index_together = (('user', 'course'),) # make search faster



# create Token automatically
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createNewToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)