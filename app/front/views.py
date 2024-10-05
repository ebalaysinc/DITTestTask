from django.shortcuts import render, redirect

def index(request):
    if 'token' in request.COOKIES: # Проверки для особо умных
        return redirect("/app/")
    else:
        return redirect("/signin/")

def sign_in(request):
    if 'token' in request.COOKIES: # Проверки для особо умных
        return redirect("/app/")
    else:
        return render(request, "signin.html")

def app(request):
    if 'token' in request.COOKIES: #... тут тоже
        return render(request, "app.html")
    else:
        return redirect("/signin/")

def title(request):
    if 'token' in request.COOKIES: # И тут
        return render(request, "title.html")
    else:
        return redirect("/signin/")

def chapter(request):   
    if 'token' in request.COOKIES: # Тут тоже, если что
        return render(request, "chapter.html")
    else:
        return redirect("/signin/")