from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserForm, CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required # декоратор функции-обработчик, для которой обязательна авторизация
from django.contrib.auth.models import User


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def snippet_page(request, snippet_id):
    context = get_base_context(request, 'Страница сниппета')
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except Snippet.DoesNotExist:
        raise Http404

    context["snippet"] = snippet
    form = CommentForm()
    context["comment_form"] = form
    return render(request, 'pages/snippet.html', context)


@login_required()
def add_snippet_page(request):
    context = get_base_context(request, 'Добавление нового сниппета')
    if request.method == 'GET':
        form = SnippetForm()
        context['form'] = form
        return render(request, 'pages/add_snippet.html', context)
    # Если POST-запрос, то мы получаем его от формы "создания сниппета"
    elif request.method == 'POST':
        form = SnippetForm(request.POST) # Форма с данными, заполненная от клиента
        if form.is_valid():
            snippet = form.save(commit=False) # вызываем объект Snippet, не сохраняя в базе данных
            # c commit=False делаем один SQL-запрос
            snippet.user = request.user # у объекта добавляем пользователя, с которого он залогинился
            snippet.save() # сохраняем сниппет с пользователем в базу данных
            return redirect('snippets')
        # Если данные не валидные, возвращаем страницу с формой и отображаем ее ошибки
        form = SnippetForm(request.POST)
        print("errors = ", form.errors)
        context['form'] = form
        return render(request, 'pages/add_snippet.html', context)


def add_comment(request):
    if request.method == "POST":
        ...


def snippet_edit(request, snippet_id):
    context = get_base_context(request, 'Редактирование сниппета')
    if request.method == "GET":
        try:
            snippet = Snippet.objects.get(id=snippet_id)
        except Snippet.DoesNotExist:
            raise Http404
        form = SnippetForm(instance=snippet)
        context['form'] = form
        context['button_name'] = 'Редактировать'
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        snippet = Snippet.objects.get(id=snippet_id)
        form = SnippetForm(request.POST, instance=snippet)
        form.save()
        return redirect('snippets')



def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.filter(public=True) # фильтрация по полю public
    context["snippets"] = snippets
    return render(request, 'pages/view_snippets.html', context)


@login_required()
def snippets_my(request):
    context = get_base_context(request, 'Мои сниппеты')
    snippets = Snippet.objects.filter(user=request.user) # отфильтровать пользователя с определенным id
    # user__username=request.user.username - фильтр по полю username
    context["snippets"] = snippets
    return render(request, 'pages/view_snippets.html', context)


def snippet_delete(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except Snippet.DoesNotExist:
        raise Http404

    snippet.delete()
    return redirect('snippets')


def create_user(request):
    context = get_base_context(request, 'Регистрация пользователя')
    if request.method == "GET":
        form = UserForm()
        context["form"] = form
        return render(request, 'pages/registration.html', context)
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #commit=False
            # user.is_active = True # в ручную открыли флаг актив для аутенфикации
            # user.set_password(user.password) # сохраняем наш пароль как хэш
            # user.save()
            return redirect('home')
        context["form"] = form
        return render(request, 'pages/registration.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            return HttpResponse("User is not found!")

    return redirect('home')



def logout_page(request):
    auth.logout(request)
    return redirect('home')