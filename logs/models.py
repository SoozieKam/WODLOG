from django.db import models
from accounts.models import *
from wods.models import Wod
from wods.models import Exercise
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator


class Log(models.Model):
    title = models.CharField(max_length=100)
    today_condition = models.CharField(max_length=50, default="좋음")
    illness = models.CharField(max_length=20, default="없음")
    illness_range = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=10),
        ],
    )
    new_date = models.CharField(max_length=8, default="20230910", unique=True)
    wod = models.ForeignKey(Wod, on_delete=models.SET_NULL, blank=True, null=True)
    exercise = models.ForeignKey(
        Exercise, on_delete=models.SET_NULL, blank=True, null=True
    )
    # pr =
    warmup = models.CharField(max_length=2000, blank=True, null=True)
    conditioning = models.CharField(max_length=2000, blank=True, null=True)
    strength = models.CharField(max_length=2000, blank=True, null=True)
    weightlifting = models.CharField(max_length=2000, blank=True, null=True)
    accessories = models.CharField(max_length=2000, blank=True, null=True)
    image = ProcessedImageField(
        upload_to="wods/", processors=[Transpose()], null=True, blank=True
    )
    video = models.FileField(upload_to="logs/videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="like_logs",
        blank=True,
        through="LikeLog",
    )
    bookmark_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="bookmark_logs",
        blank=True,
        through="BookmarkLog",
    )
    views = models.IntegerField(default=0)

    visibility = models.CharField(
        max_length=20,
        default="비공개",
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight_unit = models.CharField(max_length=10, blank=True, null=True)

    time = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    time_unit = models.CharField(max_length=10, blank=True, null=True)

    def display_weight(self):
        return f"{self.weight} {self.weight_unit}"

    def display_time(self):
        return f"{self.time} {self.time_unit}"


class LikeLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)

    class Meta:
        db_table = "like_log"


class BookmarkLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wod = models.ForeignKey(Log, on_delete=models.CASCADE)

    class Meta:
        db_table = "bookmark_log"
