from django.shortcuts import render, redirect ,get_object_or_404
from .models import Notecreate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'landing.html')

@login_required
def all(request):
    user = request.user
    notes = Notecreate.objects.filter(user=user)
    return render(request, "allnote.html", {'notes': notes})

@login_required
def create_note(request):
    user = request.user
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Notecreate.objects.create(title=title, content=content, user=user)
        return redirect("all") #Ensure 'all_note' is a valid URL name
    # notes = Notecreate.objects.all()
    return render(request, "noteedit.html")

@login_required
def edit_note(request, note_id):
    user = request.user
    note = get_object_or_404(Notecreate, id=note_id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        note.title = title
        note.content = content
        note.save()
        return redirect("all")
    return render(request, "noteedit.html", {"note": note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Notecreate, id=note_id)
    note.delete()
    return redirect("all")


def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect("login_user")
    return render(request, "signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            return redirect("all")
    return render(request, "login.html")
