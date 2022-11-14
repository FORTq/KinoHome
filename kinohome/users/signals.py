from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import *





@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)




@receiver(post_save, sender=CustomUser)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()



