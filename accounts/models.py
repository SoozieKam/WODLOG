from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image as A_Image

# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill


class User(AbstractUser):
    email = models.EmailField("이메일", blank=False)
    nickname = models.CharField("닉네임", max_length=8, blank=False, null=True)
    followers = models.ManyToManyField(
        "self", related_name="followings", symmetrical=False
    )

    def image_path(instance, filename):
        return f"accounts/profile/{instance.pk}/{filename}"

    profile_image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def process_image(profile_image):
        img = A_Image.open(profile_image)

        # 회전 메타데이터를 확인하여 이미지 회전
        if hasattr(img, "_getexif") and img._getexif():
            exif = dict(img._getexif().items())
            orientation = exif.get(0x0112)

            if orientation == 3:
                img = img.rotate(180, expand=True)
            elif orientation == 6:
                img = img.rotate(-90, expand=True)
            elif orientation == 8:
                img = img.rotate(90, expand=True)

        # 이미지 처리 및 저장
        img.thumbnail((800, 800))  # 이미지 크기 조정
        img.save(profile_image.path)


class WodRecord(models.Model):
    WOD_CHOICES = [
        ("Clean and Jerk", "Clean and Jerk"),
        ("Snatch", "Snatch"),
        ("Back Squat", "Back Squat"),
        ("Deadlift", "Deadlift"),
        ("Shoulder Press", "Shoulder Press"),
        ("Fran", "Fran"),
        ("Grace", "Grace"),
        ("Helen", "Helen"),
        ("Max Pullup", "Max Pullup"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wod_records")
    wod_name = models.CharField("운동 이름", max_length=50, choices=WOD_CHOICES, blank=True)
    date = models.DateField("날짜")
    record = models.CharField("기록", max_length=20)

    #    def save(self, *args, **kwargs):
    #        if self.wod_name and self.custom_wod_name:
    #            raise ValueError("운동 이름은 하나만 선택해야 합니다.")
    #        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.user.username} - {self.wod_name} 기록 : {self.record} ({self.date})"
        )
