import os

from django.db.models.signals import pre_save, pre_delete
from django.dispatch.dispatcher import receiver
from django.core.files.storage import default_storage
from django.conf import settings

from core.models import Post, Profile

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    """
    Deletes the image associated with the post when the post is deleted.
    """
    # Get the path of the image file.
    image_path = instance.image.path

    # If the image file exists, delete it.
    if os.path.exists(image_path):
        os.remove(image_path)

@receiver(pre_save, sender=Profile)
def delete_old_profile_image(sender, instance, **kwargs):
    """
    Deletes the old profile image when the profile image is updated.
    """
    if not instance.pk:
        return False

    try:
        old_image = Profile.objects.get(pk=instance.pk).profile_img
    except Profile.DoesNotExist:
        return False

    new_image = instance.profile_img
    if not old_image == new_image:
        # If the old image is not the default profile image, delete it.
        if os.path.exists(old_image.path) and old_image.path != os.path.join(settings.MEDIA_ROOT, 'defualt-user.png'):
            os.remove(old_image.path)
        else:
            # If the old image does not exist in the file system, delete it from the default storage.
            default_storage.delete(old_image.name)

@receiver(pre_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    """
    Deletes the profile image associated with the profile when the profile is deleted.
    """
    profile_image = instance.profile_img
    if profile_image:
        # Check if the profile image being deleted is the default image
        if profile_image.path == os.path.join(settings.MEDIA_ROOT, 'default_profile.png'):
            return
        # If the profile image exists in the file system, delete it.
        elif os.path.exists(profile_image.path):
            os.remove(profile_image.path)
        else:
            # If the profile image does not exist in the file system, delete it from the default storage.
            default_storage.delete(profile_image.name)
