from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


def post_image_path(instance, filename):
    return f'profile/{instance.username}.jpg'


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='follower', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    image = ProcessedImageField(
        upload_to=post_image_path,  # 저장 위치
        processors=[ResizeToFill(512, 512)],  # 처리할 작업 목록
        format='JPEG',  # 저장 포맷(확장자)
        options={'quality': 90},  # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
        null=True,
        blank=True,
        default='profile/default.png'
    )

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(512, 512)],  # 처리할 작업 목록
        format='JPEG',  # 저장 포맷(확장자)
        options={'quality': 90},  # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
    )
