from django import template
from core.models import Profile

register = template.Library()

@register.simple_tag
def profile_img(user_id):
    profile = Profile.objects.get(user=user_id)
    return profile.profile_img.url