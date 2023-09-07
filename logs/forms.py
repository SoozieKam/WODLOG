from django import forms
from .models import *


class dateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))


class LogForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ("오늘 PR할 거 같아요!!", "오늘 PR할 거 같아요!!"),
        ("상쾌해요!", "상쾌해요!"),
        ("그저 그래요", "그저 그래요"),
        ("몸이 무거워요", "몸이 무거워요"),
        ("못 일어나겠어요", "못 일어나겠어요"),
    ]

    ILLNESS_CHOICES = [
        ("하나도 안아파요!", "하나도 안아파요!"),
        ("머리", "머리"),
        ("어깨", "어깨"),
        ("승모", "승모"),
        ("목", "목"),
        ("등", "등"),
        ("삼두", "삼두"),
        ("이두", "이두"),
        ("전완", "전완"),
        ("팔꿈치", "팔꿈치"),
        ("손목", "손목"),
        ("허리", "허리"),
        ("복근", "복근"),
        ("대퇴사두", "대퇴사두"),
        ("햄스트링", "햄스트링"),
        ("둔근", "둔근"),
        ("무릎", "무릎"),
        ("종아리", "종아리"),
        ("발목", "발목"),
        ("손가락", "손가락"),
    ]

    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
    )
    warmup = forms.CharField(
        label="웜업",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
        help_text="고강도 훈련을 하기 전 필수! 웜업을 하면서 몸을 깨워 보세요.",
    )

    conditioning = forms.CharField(
        label="컨디셔닝",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
        help_text="유산소 운동과 무산소 운동이 함꼐 있는 운동으로, 보통 박스에서 하는 와드를 적으면 됩니다.",
    )

    strength = forms.CharField(
        label="스트렝스",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
        help_text="최대 근력을 키우는 데 집중하는 운동으로, 고중량 3대 운동이나 프레스 등이 해당됩니다.",
    )

    weightlifting = forms.CharField(
        label="역도",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
        help_text="클린, 스내치 뿐만 아니라 스내치 발란스나 클린 풀 등 훈련을 하면 여기 적어주세요.",
    )

    accessories = forms.CharField(
        label="추가 운동",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
    )

    today_condition = forms.ChoiceField(label="오늘 컨디션", choices=CONDITION_CHOICES)
    illness = forms.ChoiceField(label="아픈 곳", choices=ILLNESS_CHOICES)
    illness_range = forms.IntegerField(
        label="아픈 정도",
    )

    image = forms.ImageField(
        label="사진", widget=forms.FileInput(attrs={"class": "border border-inherit"})
    )

    video = forms.FileField(
        label="영상", widget=forms.FileInput(attrs={"class": "border border-inherit"})
    )

    visibility = forms.CharField(label="공개 범위")

    class Meta:
        model = Log
        exclude = (
            "wod",
            "like_users",
            "bookmark_users",
            "created_at",
            "updated_at",
            "views",
            "owner",
        )
