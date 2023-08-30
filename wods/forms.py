from django import forms
from .models import *


class WodForm(forms.ModelForm):
    CATEGORY_SCORE_CHOICES = [
        ("For reps", "For reps"),
        ("For time", "For time"),
        ("EMOM", "EMOM"),
        ("AMRAP", "AMRAP"),
        ("For Load", "For Load"),
        ("For Quality", "For Quality"),
        ("Tabata", "Tabata"),
    ]

    CATEGORY_PPL_CHOICES = [
        ("1", "1"),
        ("Team of 2", "Team of 2"),
        ("Team of 3", "Team of 3"),
        ("Team of 4", "Team of 4"),
        ("Team of 5", "Team of 5"),
        ("Team of 6", "Team of 6"),
    ]

    CATEGORY_SPECIAL_CHOICES = [
        ("Classic Benchmarks", "Classic Benchmarks"),
        ("Memorials, Tributes, & Holidays", "Memorials, Tributes, & Holidays"),
        ("The Heroes", "The Heroes"),
        ("Coach Creations", "Coach Creations"),
    ]

    name = forms.CharField(
        label="와드명",
        widget=forms.TextInput(
            attrs={
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
    )
    content = forms.CharField(
        label="구성",
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "pattern": ".{1,}",
                "required": "true",
                "class": "invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500 peer",
            }
        ),
    )

    cate_score = forms.ChoiceField(label="와드 방식", choices=CATEGORY_SCORE_CHOICES)
    cate_ppl = forms.ChoiceField(label="인원수", choices=CATEGORY_PPL_CHOICES)
    cate_special = forms.ChoiceField(label="카테고리", choices=CATEGORY_SPECIAL_CHOICES)

    image = forms.ImageField(
        label="사진", widget=forms.FileInput(attrs={"class": "border border-inherit"})
    )

    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        label="동작",
        widget=forms.CheckboxSelectMultiple(),
    )
    # widget=forms.CheckboxSelectMultiple(),

    equips = forms.ModelMultipleChoiceField(
        queryset=Equip.objects.all(),
        label="도구",
        widget=forms.CheckboxSelectMultiple(),
    )
    time = forms.IntegerField(
        label="타임캡",
    )

    class Meta:
        model = Wod
        fields = (
            "name",
            "content",
            "time",
            "cate_score",
            "cate_ppl",
            "cate_special",
            "image",
            "exercises",
            "equips",
        )


class WodReviewForm(forms.ModelForm):
    class Meta:
        model = WodReview
        fields = ("content",)


# WodExerciseFormSet = forms.inlineformset_factory(
#     Wod,
#     WodExercise,
#     fields=("exercises",),
#     extra=1,
#     can_delete=False,
#     labels={"포함된 동작": ""},
# )

# wod update form

# class EquipForm(forms.ModelForm):
#     class Meta:
#         model = Equip
#         fields = (
#             "abike",
#             "barbell",
#             "bench",
#             "bikeerg",
#             "box",
#             "d_ball",
#             "dip_bar",
#             "dumbbell",
#             "ghd_machine",
#             "gymnastic_rings",
#             "jump_rope",
#             "kettlebell",
#             "wallball",
#             "pullup_bar",
#             "rope",
#             "rower",
#             "sandbag",
#             "skierg",
#             "sled",
#             "treadmill",
#             "weight_rack",
#             "weight_vest",
#             "wall",
#             "worm",
#         )
#         labels = {
#             "abike": "어썰트바이크",
#             "barbell": "바벨",
#             "bench": "벤치",
#             "bikeerg": "바이크에르그",
#             "box": "박스",
#             "d_ball": "디볼",
#             "dip_bar": "딥스 바",
#             "dumbbell": "덤벨",
#             "ghd_machine": "GHD 머신",
#             "gymnastic_rings": "링",
#             "jump_rope": "줄넘기",
#             "kettlebell": "케틀벨",
#             "wallball": "메디신볼(월볼)",
#             "pullup_bar": "풀업 바",
#             "rope": "로프",
#             "rower": "로잉",
#             "sandbag": "샌드백",
#             "skierg": "스키에르그",
#             "sled": "슬레드",
#             "treadmill": "트레드밀",
#             "wall": "벽",
#             "weight_rack": "랙",
#             "weight_vest": "중량조끼",
#             "worm": "웜",
#         }
