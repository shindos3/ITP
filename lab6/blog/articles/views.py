from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
        # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
        # в словаре form будет храниться информация, введенная пользователем
            if not Article.objects.get(title=form["title"]):
                if form["text"] and form["title"]:
        # если поля заполнены без ошибок
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
                else:
                    # если введенные данные некорректны
                    form['errors'] = u"Не все поля заполнены"
                    return render(request, 'create_post.html', {'form': form})
            else:
        # если введенные данные некорректны
                form['errors'] = u"Название статьи должно быть уникально!"
                return render(request, 'create_post.html', {'form': form})
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404

def registration(request):
    if request.user.is_anonymous:
        if request.method == "POST":
        # обработать данные формы, если метод POST

            form = {
                'login': request.POST.get("login"), 'email': request.POST.get("email"), 'passwd': request.POST.get("passwd")
            }
        # в словаре form будет храниться информация, введенная пользователем
            try:
                User.objects.get(email=form["email"])
                # если пользователь существует, то ошибки не произойдет и программа # удачно доберется до следующей строчки
                form['errors'] = u"Пользователь с тким email уже зарегистрирован!"
                return render(request, 'registration.html', {'form': form})
            except User.DoesNotExist:
                if form["login"] and form["email"] and form["passwd"]:
                    # если поля заполнены без ошибок
                    User.objects.create_user(form["login"], form["email"], form["passwd"])
                    return redirect('archive')
                    # перейти на главную
                else:
                    # если введенные данные некорректны
                    form['errors'] = u"Не все поля заполнены"
                    return render(request, 'registration.html', {'form': form})


        # если введенные данные некорректны

        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'registration.html', {})
    else:
    # просто вернуть страницу с формой, если метод GET
        return redirect('archive')

def login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
        # обработать данные формы, если метод POST

            form = {
                'login': request.POST.get("login"), 'passwd': request.POST.get("passwd")
            }
        # в словаре form будет храниться информация, введенная пользователем
            if  form["login"] and form["passwd"]:
                # если поля заполнены без ошибок
                user = authenticate(username=form["login"], password=form["passwd"])

                if user:
                    auth_login(request, user)
                    return redirect('archive')
                # перейти на главную
                else:
                    # если введенные данные некорректны
                    form['errors'] = u"Пользователь не существует!"
                    return render(request, 'login.html', {'form': form})
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'login.html', {'form': form})


        # если введенные данные некорректны

        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'login.html', {})
    else:
    # просто вернуть страницу с формой, если метод GET
        return redirect('archive')
