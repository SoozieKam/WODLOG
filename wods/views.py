from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import os, json
import requests
import pprint
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q
from django.db.models import Count


# Create your views here.
def index(request):
    wods = Wod.objects.all()
    #    sum_amount = Wod.objects.aggregate(Sum('amount'))

    exercises = Exercise.objects.all()

    forreps_wods = Wod.objects.filter(cate_score="For reps")
    fortime_wods = Wod.objects.filter(cate_score="For time")
    emom_wods = Wod.objects.filter(cate_score="EMOM")
    amrap_wods = Wod.objects.filter(cate_score="AMRAP")
    forload_wods = Wod.objects.filter(cate_score="For load")
    forquality_wods = Wod.objects.filter(cate_score="For quality")
    tabata_wods = Wod.objects.filter(cate_score="Tabata")

    single_wods = Wod.objects.filter(cate_ppl="1")
    to2_wods = Wod.objects.filter(cate_ppl="Team of 2")
    to3_wods = Wod.objects.filter(cate_ppl="Team of 3")
    to4_wods = Wod.objects.filter(cate_ppl="Team of 4")
    to5_wods = Wod.objects.filter(cate_ppl="Team of 5")
    to6_wods = Wod.objects.filter(cate_ppl="Team of 6")

    classic_wods = Wod.objects.filter(cate_special="Classic Benchmarks")
    mth_wods = Wod.objects.filter(cate_special="Memorials, Tributes, & Holidays")
    heroes_wods = Wod.objects.filter(cate_special="The heroes")
    coach_wods = Wod.objects.filter(cate_special="Coach Creations")

    context = {
        "wods": wods,
        "exercises": exercises,
        "forreps_wods": forreps_wods,
        "fortime_wods": fortime_wods,
        "emom_wods": emom_wods,
        "amrap_wods": amrap_wods,
        "forload_wods": forload_wods,
        "forquality_wods": forquality_wods,
        "tabata_wods": tabata_wods,
        "single_wods": single_wods,
        "to2_wods": to2_wods,
        "to3_wods": to3_wods,
        "to4_wods": to4_wods,
        "to5_wods": to5_wods,
        "to6_wods": to6_wods,
        "classic_wods": classic_wods,
        "mth_wods": mth_wods,
        "heroes_wods": heroes_wods,
        "coach_wods": coach_wods,
    }
    return render(request, "wods/index.html", context)


def detail(request, wod_id):
    wod = Wod.objects.get(pk=wod_id)
    exercises = wod.exercises.all()
    equips = wod.equips.all()
    # exercises = WodExercise.objects.filter(wod=wod)
    # print(exercises)

    context = {
        "wod": wod,
        "exercises": exercises,
        "equips": equips,
    }

    return render(request, "wods/detail.html", context)


def create(request):
    exercises = Exercise.objects.all()

    if request.method == "POST":
        form = WodForm(request.POST, request.FILES)
        # formset = WodExerciseFormSet(request.POST)

        if form.is_valid():
            wod = form.save(commit=False)
            wod.user = request.user
            wod.save()
            form.save_m2m()  # Save the many-to-many relationships (exercises)

            # print(wod.exercises)

            # if formset.is_valid():
            #     formset.instance = wod
            #     formset.save()

            return redirect("wods:detail", wod_id=wod.pk)
    else:
        form = WodForm()
        # formset = WodExerciseFormSet()

    context = {
        "form": form,
        # "formset": formset,
        "exercises": exercises,
    }

    return render(request, "wods/create.html", context)


def delete(request, wod_id):
    wod = get_object_or_404(Wod, pk=wod_id)

    if request.method == "POST":
        wod.delete()
        return redirect("wods:index")

    context = {
        "wod": wod,
    }

    return render(request, "wods/delete.html", context)


def likes(request, wod_id):
    wod = get_object_or_404(Wod, pk=wod_id)

    if wod.like_users.filter(pk=request.user.pk).exists():
        wod.like_users.remove(request.user)
        is_liked = False
    else:
        wod.like_users.add(request.user)
        is_liked = True

    context = {
        "is_liked": is_liked,
    }

    return JsonResponse(context)


def bookmark(request, wod_id):
    wod = get_object_or_404(Wod, pk=wod_id)

    if wod.bookmark_users.filter(pk=request.user.pk).exists():
        wod.bookmark_users.remove(request.user)
        is_bookmarked = False
    else:
        wod.like_users.add(request.user)
        is_bookmarked = True

    context = {"is_bookmarked": is_bookmarked}

    return JsonResponse(context)


def search(request):
    keyword = request.GET.get("keyword")
    print(keyword)

    # 와드 이름에 키워드가 포함된 레시피들 쿼리셋
    name_queryset = Wod.objects.filter(name__icontains=keyword)

    # 동작에 키워드가 포함된 레시피들 쿼리셋
    exercise_queryset = Wod.objects.filter(exercises__name__icontains=keyword)

    context = {
        "keyword": keyword,
        "name_wods": name_queryset,
        "exercise_wods": exercise_queryset,
    }

    return render(request, "wods/search.html", context)


def search_by_name(request):
    keyword = request.GET.get("keyword")
    sort_param = request.GET.get("sort")

    if keyword:
        name_queryset = Wod.objects.filter(name__icontains=keyword).order_by(
            "-created_at"
        )

        if sort_param == "created_at_asc":
            name_queryset = name_queryset.order_by("-created_at")
        elif sort_param == "created_at_desc":
            name_queryset = name_queryset.order_by("created_at")
        elif sort_param == "time_asc":
            name_queryset = name_queryset.order_by("time")
        elif sort_param == "time_desc":
            name_queryset = name_queryset.order_by("-time")
        elif sort_param == "likes_asc":
            name_queryset = name_queryset.annotate(
                num_likes=Count("like_wods")
            ).order_by("num_likes")
        elif sort_param == "likes_desc":
            name_queryset = name_queryset.annotate(
                num_likes=Count("like_wods")
            ).order_by("-num_likes")
        elif sort_param == "views_asc":
            name_queryset = name_queryset.annotate(
                num_views=Count("viewed_wods")
            ).order_by("num_views")
        elif sort_param == "views_desc":
            name_queryset = name_queryset.annotate(
                num_views=Count("viewed_wods")
            ).order_by("-num_views")

    else:
        name_queryset = Wod.objects.all().order_by("-created_at")
        sort_param = None

    # 포함하는 동작, 제외하는 동작
    include_exercise = request.GET.getlist("include_exercise")
    exclude_exercise = request.GET.getlist("exclude_exercise")

    print(include_exercise)
    print(exclude_exercise)

    wods = Wod.objects.all()
    q = Q()

    if include_exercise:
        q &= Q(exercises__name__in=include_exercise)

    if exclude_exercise:
        q &= ~Q(exercises__name__in=exclude_exercise)

    q_wods = Wod.objects.filter(q)

    context = {
        "wods": wods,
        "keyword": keyword,
        "name_wods": name_queryset,
        "sort_param": sort_param,
        "q_wods": q_wods,
    }

    return render(request, "wods/search_by_name.html", context)


# def search_by_exercise(request):
#     keyword = request.GET.get("keyword")
#     sort_param = request.GET.get("sort")

#     exercise_queryset = Wod.objects.filter(exercises__name__icontains=keyword)

#     if sort_param == "created_at_asc":
#         exercise_queryset = exercise_queryset.order_by("-created_at")
#     elif sort_param == "created_at_desc":
#         exercise_queryset = exercise_queryset.order_by("created_at")
#     elif sort_param == "time_asc":
#         exercise_queryset = exercise_queryset.order_by("time")
#     elif sort_param == "time_desc":
#         exercise_queryset = exercise_queryset.order_by("-time")
#     # elif sort_param == "likes_asc":
#     #     exercise_queryset = exercise_queryset.annotate(num_likes=Count("like_wods")).order_by(
#     #         "num_likes"
#     #     )
#     # elif sort_param == "likes_desc":
#     #     exercise_queryset = exercise_queryset.annotate(num_likes=Count("like_wods")).order_by(
#     #         "-num_likes"
#     #     )
#     # elif sort_param == "views_asc":
#     #     exercise_queryset = exercise_queryset.annotate(num_views=Count("viewed_wods")).order_by(
#     #         "num_views"
#     #     )
#     # elif sort_param == "views_desc":
#     #     exercise_queryset = exercise_queryset.annotate(num_views=Count("viewed_wods")).order_by(
#     #         "-num_views"
#     #     )

#     context = {
#         "keyword": keyword,
#         "exercise_wods": exercise_queryset,
#         "sort_param": sort_param,
#     }

#     return render(request, "wods/search_by_exercise.html", context)
