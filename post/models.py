from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

from user.models import User


# 게시글 이미지의 저장 위치 경로를 생성해주는 함수
def post_image_path(instance, filename):
    return f'postings/{instance.author}/{instance.create_at}.jpg'


# 게시글 모델
class Post(models.Model):
    class Meta:
        ordering = ['-create_at', ]

    content = models.TextField(verbose_name="내용", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    like = models.ManyToManyField(User, related_name='post_like', blank=True)
    image = ProcessedImageField(
        upload_to=post_image_path,  # 저장 위치
        processors=[ResizeToFill(1024, 1024)],  # 처리할 작업 목록
        format='JPEG',  # 저장 포맷(확장자)
        options={'quality': 90},  # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
    )

    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(512, 512)],  # 처리할 작업 목록
        format='JPEG',  # 저장 포맷(확장자)
        options={'quality': 90},  # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
    )
