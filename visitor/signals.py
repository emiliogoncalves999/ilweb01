from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from log.models import LogEntry

User = get_user_model()

# @receiver(post_save)
# def log_save(sender, instance, created, **kwargs):
#     if sender == LogEntry:
#         return

#     action = 'CREATE' if created else 'UPDATE'
#     user = kwargs.get('user')

#     # Attempt to retrieve user if not provided
#     if user is None:
#         user_id = getattr(instance, 'user_id', None)
#         if user_id:
#             try:
#                 user = User.objects.get(pk=user_id)
#             except User.DoesNotExist:
#                 user = None

#     # Log the action
#     LogEntry.objects.create(
#         action=action,
#         model_name=sender.__name__,
#         instance_id=str(instance.pk),
#         user=user,
#         details=f"Data: {instance.__dict__}"
#     )

# @receiver(post_delete)
# def log_delete(sender, instance, **kwargs):
#     if sender == LogEntry:
#         return

#     user = kwargs.get('user')

#     # Attempt to retrieve user if not provided
#     if user is None:
#         user_id = getattr(instance, 'user_id', None)
#         if user_id:
#             try:
#                 user = User.objects.get(pk=user_id)
#             except User.DoesNotExist:
#                 user = None

#     # Log the action
#     LogEntry.objects.create(
#         action='DELETE',
#         model_name=sender.__name__,
#         instance_id=str(instance.pk),
#         user=user,
#         details=f"Data: {instance.__dict__}"
#     )
