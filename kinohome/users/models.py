from django.db import models
from django.contrib.auth.models import AbstractUser


from home.models import Kino
# Create your models here.





class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.user.username


class Favorites(models.Model):
    user_f = models.ForeignKey(CustomUser, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='list_user_kino_favorites')
    kino = models.ForeignKey(Kino, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='list_favor_kino_favorites')


    def save(self, *args, **kwargs):
        super(Favorites, self).save(*args, **kwargs)


class Plans(models.Model):
    user_f = models.ForeignKey(CustomUser, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='list_user_kino_plans')
    kino = models.ForeignKey(Kino, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='list_plan_kino_plans')


    def save(self, *args, **kwargs):
        super(Plans, self).save(*args, **kwargs)



class EmailSub(models.Model):
    email = models.EmailField(max_length=254, null=True)




