from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.user.models import TeamUser, UserProfileInfo

@receiver(post_save, sender=TeamUser)
def create_user_profile(sender, instance, created , **kwargs):
    if created:
        UserProfileInfo.objects.create(user=instance)
