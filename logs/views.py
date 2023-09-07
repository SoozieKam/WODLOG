from django.shortcuts import render, redirect
from .models import *
from .forms import *
from wods.models import Exercise
from wods.models import Wod
from datetime import date

# Create your views here.


def calendar(request):
    today = date.today()
    selected_date = request.POST.get("selected_date")

    context = {
        "today": today,
        "selected_date": selected_date,
    }
    return render(request, "logs/calendar.html", context)


def write(request, selected_date):
    wods = Wod.objects.all()
    exercises = Exercise.objects.all()

    if request.method == "POST":
        form = LogForm(request.POST, request.FILES)

        if form.is_valid():
            log = form.save(commit=False)
            log.owner = request.user
            log.save()

            return redirect("logs:calendar")
    else:
        form = LogForm()

    context = {
        "form": form,
        "exercises": exercises,
        "wods": wods,
    }

    return render(request, "logs/write.html", context)
