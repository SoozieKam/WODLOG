from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose


# lower body, upper body, core, weightlifting, gymnastic, machine은 태그로
# lower body
# squatting
# lunging
# hinging

# upper body
# pulling
# pressing

# core

# weightlifting


class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Equip(models.Model):
    name = models.CharField(max_length=100, default="도구")

    # wod = models.OneToOneField(Wod, on_delete=models.CASCADE, default=None)
    # abike = models.BooleanField(default=False)
    # barbell = models.BooleanField(default=False)
    # bench = models.BooleanField(default=False)
    # bikeerg = models.BooleanField(default=False)
    # box = models.BooleanField(default=False)
    # d_ball = models.BooleanField(default=False)
    # dip_bar = models.BooleanField(default=False)
    # dumbbell = models.BooleanField(default=False)
    # ghd_machine = models.BooleanField(default=False)
    # gymnastic_rings = models.BooleanField(default=False)
    # jump_rope = models.BooleanField(default=False)
    # kettlebell = models.BooleanField(default=False)
    # wallball = models.BooleanField(default=False)
    # pullup_bar = models.BooleanField(default=False)
    # rope = models.BooleanField(default=False)
    # rower = models.BooleanField(default=False)
    # sandbag = models.BooleanField(default=False)
    # skierg = models.BooleanField(default=False)
    # sled = models.BooleanField(default=False)
    # treadmill = models.BooleanField(default=False)
    # wall = models.BooleanField(default=False)
    # weight_rack = models.BooleanField(default=False)
    # weight_vest = models.BooleanField(default=False)
    # worm = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Wod(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, blank=True, null=True)
    cate_score = models.CharField(max_length=50, blank=True, null=True)
    cate_ppl = models.CharField(max_length=50, blank=True, null=True)
    cate_special = models.CharField(max_length=50, blank=True, null=True)
    image = ProcessedImageField(
        upload_to="wods/", processors=[Transpose()], null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="like_wods",
        blank=True,
        through="LikeWod",
    )
    bookmark_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="bookmark_wods",
        blank=True,
        through="BookmarkWod",
    )
    exercises = models.ManyToManyField(Exercise, through="WodExercise")
    equips = models.ManyToManyField(Equip, through="WodEquip")

    views = models.IntegerField(default=0)
    time = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class LikeWod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)

    class Meta:
        db_table = "like_wod"


class BookmarkWod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)

    class Meta:
        db_table = "bookmark_wod"


class WodExercise(models.Model):
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class WodEquip(models.Model):
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE)
    equips = models.ForeignKey(Equip, on_delete=models.CASCADE)


class WodReview(models.Model):
    wod = models.ForeignKey(Wod, on_delete=models.CASCADE, related_name="wods")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 와드로그에 쓰기 위해 와드 내용을 담아가야 함 이거 추가 !
