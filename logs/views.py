from django.shortcuts import render, redirect
from .models import *
from .forms import *
from wods.models import Exercise
from wods.models import Wod
from datetime import date

# Create your views here.


def calendar(request):
    today = date.today()
    logs = Log.objects.all()
    selected_date = request.GET.get("selected_date")
    request.session["selected_date"] = selected_date

    # selected_date = request.POST.get("selected_date")
    # print(selected_date)

    context = {
        "today": today,
        "logs": logs,
        #    "selected_date": selected_date,
    }
    return render(request, "logs/calendar.html", context)


def write(request):
    wods = Wod.objects.all()
    exercises = Exercise.objects.all()
    selected_date = request.GET.get("selected_date", None)
    # my = {"new_date": selected_date}
    print(selected_date)

    if request.method == "POST":
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST.get("selected_date"))
            log = form.save(commit=False)
            log.owner = request.user
            print(log.new_date)
            # log.new_date = selected_date  # Log 모델의 date 필드에 선택한 날짜를 저장
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
