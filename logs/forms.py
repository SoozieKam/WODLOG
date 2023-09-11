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

    VISIBILITY_CHOICES = [
        ("전체 공개", "전체 공개"),
        ("친구 공개", "친구 공개"),
        ("비공개", "비공개"),
    ]

    # 무게 단위 선택 옵션
    WEIGHT_CHOICES = [
        ("lbs", "lbs"),
        ("kg", "kg"),
    ]

    # 시간 단위 선택 옵션
    TIME_CHOICES = [
        ("시간", "시간"),
        ("분", "분"),
        ("초", "초"),
        ("개", "개"),
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
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
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
    )
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(),
        label="PR한 동작",
        required=False,
        widget=forms.Select(),
    )
    weight = forms.DecimalField(label="무게", required=False)
    weight_unit = forms.ChoiceField(label="단위", choices=WEIGHT_CHOICES, required=False)

    wod = forms.ModelChoiceField(
        queryset=Wod.objects.all(),
        label="PR한 와드",
        required=False,
        widget=forms.Select(),
    )
    time = forms.DecimalField(label="시간 (렙 수)", required=False)
    time_unit = forms.ChoiceField(label="단위", choices=TIME_CHOICES, required=False)

    today_condition = forms.ChoiceField(label="오늘 컨디션", choices=CONDITION_CHOICES)
    illness = forms.ChoiceField(label="아픈 곳", required=False, choices=ILLNESS_CHOICES)
    illness_range = forms.IntegerField(
        label="아픈 정도",
        required=False,
    )

    image = forms.ImageField(
        label="사진",
        required=False,
        widget=forms.FileInput(attrs={"class": "border border-inherit"}),
    )

    video = forms.FileField(
        label="영상",
        required=False,
        widget=forms.FileInput(attrs={"class": "border border-inherit"}),
    )

    visibility = forms.ChoiceField(label="공개 범위", choices=VISIBILITY_CHOICES)
    new_date = forms.HiddenInput()

    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)
        # wod 필드의 label을 wod.name으로 설정
        self.fields["wod"].label_from_instance = lambda obj: obj.name

    class Meta:
        model = Log
        exclude = (
            "like_users",
            "bookmark_users",
            "created_at",
            "updated_at",
            "views",
            "owner",
            "new_date",
        )
