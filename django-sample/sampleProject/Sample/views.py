from django.shortcuts import render


def index(request):
    data = {"fullName": "Насибулин Самир Дамирович", "school": "Алабуга Политех", "group": "215-8.2", "spec": "Веб-Дизайн и Разработка", "plans": "Хочу быть после выпуска ..."}
    return render(request, "index.html", {'data': data})


def about(request):
    info = {"fullName": "Насибулин Самир Дамирович", "growth": "Рост:170 см", "weight": "58 kg", "age": "16 лет"}
    return render(request, "about.html", {'info': info})


def contact(request):
    contact = {"tg": "https://t.me/paddonrobo", "phone": "+79508363506"}
    return render(request, "contact.html", {'contact': contact})

def form(request):
    return render(request, 'form.html')