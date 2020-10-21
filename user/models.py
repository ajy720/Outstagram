from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


# 게시글 이미지의 저장 위치 경로를 생성해주는 함수
def post_image_path(instance, filename):
    return f'profile/{instance.username}.jpg'


# 회원 모델, AbstractUser를 상속 받아 Customize 했다.
class User(AbstractUser):
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

    def __str__(self):
        return self.username

    # 팔로워를 반환하는 함수
    def get_followers(self):
        return [user.user_from for user in self.followers.all()]

    # 팔로이를 반환하는 함수
    def get_following(self):
        return [user.user_to for user in self.following.all()]


# 사용자 팔로우 관계 모델
class UserFollowing(models.Model):
    class Meta:
        unique_together = ("user_from", "user_to")

    user_from = models.ForeignKey("User", related_name="following",
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey("User", related_name="followers",
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
