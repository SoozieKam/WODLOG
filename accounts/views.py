from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
)

# from django.contrib.auth.forms import PasswordChangeForm
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomAuthenticationForm,
    WodRecordForm,
)
from django.core.paginator import Paginator


def login(request):
    if request.user.is_authenticated:
        return redirect("wods:index")

    if request.method == "POST":
        # 사용자가 제출한 폼 데이터를 바탕으로 CustomAuthenticationForm 인스턴스 생성
        # 사용자가 제출한 데이터를 'request.POST'에서 가져와서 사용자를 로그인시키려면 'request'가 필요
        form = CustomAuthenticationForm(request, request.POST)

        if form.is_valid():
            # form.get_user()로부터 인증된 사용자 객체를 가져와서 사용자를 로그인시킴.
            # auth_login() 함수는 Django의 내장 함수이며, 인증된 사용자를 로그인 시키는 역할을 함.
            auth_login(request, form.get_user())

            # 이전에 방문한 페이지의 URL을 세션(Session)에서 가져옵니다.
            prev_url = request.session.get("prev_url")

            if prev_url:
                # 이전 페이지 URL 삭제
                del request.session["prev_url"]
                # 만약 이전 페이지 URL이 세션에 저장되어 있다면, 해당 URL로 리다이렉트.
                # 이를 통해 로그인 후 이전 페이지로 돌아가는 기능 구현.
                return redirect(prev_url)
            return redirect("wods:index")

    # POST가 아니라 GET 방식의 HTTP 요청일 경우 (즉 사용자가 로그인 폼을 제출하지 않았을 경우)
    else:
        # 빈 로그인 폼 생성. 사용자가 로그인 폼을 제출하지 않았을 때 기본적으로 보여주는 로그인 폼.
        form = CustomAuthenticationForm()

        # 사용자가 로그인 폼을 보기 전에 방문한 페이지 URL을 세션에 저장. 이를 통해 로그인 후 이전 페이지로 돌아가는 기능 구현 가능!
        request.session["prev_url"] = request.META.get("HTTP_REFERER")

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("wods:index")


def signup(request):
    if request.user.is_authenticated:
        return redirect("wods:index")

    if request.method == "POST":
        # 사용자가 제출한 데이터와 업로드한 파일을 폼 객체로 바꿔서 CustomUserCreationForm 인스턴스를 생성
        # Request.POST는 폼에 입력한 텍스트 데이터를 담고 있음.
        # 사용자가 폼에서 입력한 텍스트 데이터는 POST 방식으로 서버로 전송되며, 이 데이터는 request.POST를 통해 접근 가능.

        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            # 방금 가입한 사용자를 로그인 시킵니다.
            auth_login(request, user)
            return redirect("wods:index")

    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/signup.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", username=request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        "form": form,
    }

    return render(request, "accounts/update.html", context)


@login_required
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    # post_list = Post.objects.filter(user=person).order_by('-pk')
    # comment_list = Comment.objects.filter(user=person).order_by('-pk')
    # recipe_list = Recipe.objects.filter(user=person).order_by('-pk')

    # recipes = person.recipe_written.all()
    # like_recipes = person.like_recipes.all()
    # bookmark_recipes = person.bookmark_recipes.all()

    # q = request.GET.get('q')

    # paginator_post = Paginator(post_list, 5)
    # post_page = request.GET.get('post_page')
    # posts = paginator_post.get_page(post_page)

    # paginator_comment = Paginator(comment_list, 5)
    # comment_page = request.GET.get('comment_page')
    # comments = paginator_comment.get_page(comment_page)

    # paginator_recipe = Paginator(recipe_list, 5)
    # recipe_page = request.GET.get('recipe_page')
    # recipes = paginator_recipe.get_page(recipe_page)

    # posts.q = q
    # comments.q = q

    context = {
        # 'posts': posts,
        # 'comments': comments,
        # 'q': q,
        "person": person,
        # 'recipes': recipes,
        # 'like_recipes': like_recipes,
        # 'bookmark_recipes': bookmark_recipes,
    }
    return render(request, "accounts/profile.html", context)
