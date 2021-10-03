from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# when we creat User , profile creat too.
# save use for update. 
@receiver(post_save, sender=User)
def creat_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#we want if we delet object from profile , it delet from user's model too.
@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()    