from django.shortcuts import render
from django.http import HttpResponse


def get_index(request):
    context = {
        "my_list": [1, 2, 3, 4, 5, "Text"],
    }
    return render(request, "posts/index.html", context=context)


def test_page(request):
    body = "<h1>Тестовая страница</h1>"
    return HttpResponse(body)


def get_contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context=context)


def get_about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "posts/about.html", context=context)
