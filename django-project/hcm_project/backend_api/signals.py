from django.db.models.signals import post_save
from django.dispatch import receiver

from hcm_project.backend_api.appuser import AppUser
from hcm_project.backend_api.models import LeaveBallance

@receiver(post_save, sender=AppUser)
def create_leave_balance(sender, instance, created, **kwargs):
    if created:
        LeaveBallance.objects.create(employee=instance)