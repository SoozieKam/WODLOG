from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
from wods.models import Exercise
from wods.models import Wod
from datetime import date
from django.core import serializers
import json
from django.shortcuts import get_object_or_404

# Create your views here.


def calendar(request):
    today = date.today()
    logs = Log.objects.all()
    # selected_date = request.GET.get("selected_date")
    # request.session["selected_date"] = selected_date

    # selected_date = request.POST.get("selected_date")
    # print(selected_date)

    context = {
        "today": today,
        "logs": logs,
        # "selected_date": selected_date,
    }
    return render(request, "logs/calendar.html", context)


def get_logs(request):
    # 로그 데이터를 가져옵니다.
    logs = Log.objects.all()

    log_data = []
    for log in logs:
        log_data.append(
            {  # 주석 처리한 건 JSON serializable하지 않은 필드들 .. 추후 해결
                "title": log.title,
                "today_condition": log.today_condition,
                "illness": log.illness,
                "illness_range": log.illness_range,
                "new_date": log.new_date,
                "warmup": log.warmup,
                "conditioning": log.conditioning,
                "strength": log.strength,
                "weightlifting": log.weightlifting,
                "accessories": log.accessories,
                # PR한 동작
                # "exercise": log.exercise,
                # "weight": log.weight,
                "weight_unit": log.weight_unit,
                # PR한 와드
                # "wod": log.wod,
                # "time": log.time,
                "time_unit": log.time_unit,
                # "image": log.image,
                # "video": log.video,
                "visibility": log.visibility,
            }
        )

    # 파이썬 딕셔너리를 JSON 문자열로 직렬화합니다.
    serialized_logs = json.dumps(log_data)
    # 데이터를 JSON 형식으로 직렬화합니다.
    # serialized_logs = serializers.serialize("json", log_data)

    # JsonResponse를 사용하여 직렬화된 데이터를 클라이언트에 반환합니다.
    return JsonResponse({"logs": serialized_logs}, safe=False)


def detail(request, log_id):
    log = get_object_or_404(Log, pk=log_id)

    # log = Log.objects.filter(pk=log_id)
    log_data = {
        "title": log.title,
        "today_condition": log.today_condition,
        "illness": log.illness,
        "illness_range": log.illness_range,
        "new_date": log.new_date,
        "warmup": log.warmup,
        "conditioning": log.conditioning,
        "strength": log.strength,
        "weightlifting": log.weightlifting,
        "accessories": log.accessories,
        # PR한 동작
        "exercise": log.exercise,
        "weight": log.weight,
        "weight_unit": log.weight_unit,
        # PR한 와드
        "wod": log.wod,
        "time": log.time,
        "time_unit": log.time_unit,
        "image": log.image,
        "video": log.video,
        "visibility": log.visibility,
    }

    return JsonResponse(log_data)


def write(request):
    wods = Wod.objects.all()
    exercises = Exercise.objects.all()
    selected_date = request.GET.get("selected_date", None)
    # my = {"new_date": selected_date}
    print(selected_date)

    if request.method == "POST":
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            selected_date = request.POST.get("new_date", None)
            print(selected_date)
            log = form.save(commit=False)
            log.owner = request.user
            print(log.new_date)
            log.new_date = selected_date  # Log 모델의 date 필드에 선택한 날짜를 저장
            print(log.new_date)

            log.save()

        return redirect("logs:calendar")
    else:
        form = LogForm()

    context = {
        "form": form,
        "exercises": exercises,
        "wods": wods,
        "selected_date": selected_date,
    }

    return render(request, "logs/write.html", context)


# def write(request):
#    wods = Wod.objects.all()
#    exercises = Exercise.objects.all()
#
#    if request.method == "POST":
#        form = LogForm(request.POST, request.FILES)
#
#        if form.is_valid():
#            if selected_date:
#                log = form.save(commit=False)
#                log.owner = request.user
#                log.new_date = selected_date
#                log.save()
#
#                return redirect("logs:calendar")
#    else:
#        form = LogForm()
#        selected_date = request.GET.get("selected_date", None)
#        selected_year = request.GET.get("year", None)
#        print(selected_year)
#        print(selected_date)
#
#    context = {
#
#        "form": form,
#        "exercises": exercises,
#        "wods": wods,
#    }
#
#    return render(request, "logs/write.html", context)
