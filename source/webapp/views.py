from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestbookForm
from webapp.models import Guestbook


def index_view(request):
    guestbooks = Guestbook.objects.order_by("-update_nt")
    context = {"guestbooks": guestbooks}
    return render(request, "index.html", context)


def create_guestbook(request):
    if request.method == "GET":
        form = GuestbookForm()
        return render(request, "create.html", {"form": form})
    else:
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get("author")
            email = form.cleaned_data.get("email")
            note = form.cleaned_data.get("note")
            Guestbook.objects.create(author=author, email=email, note=note)
            return redirect("index")
        return render(request, "create.html", {"form": form})


def update_guestbook(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        form = GuestbookForm(initial={
            "author": guestbook.author,
            "email": guestbook.email,
            "note": guestbook.note
        })
        return render(request, "update.html", {"form": form})
    else:
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            guestbook.author = form.cleaned_data.get("author")
            guestbook.email = form.cleaned_data.get("email")
            guestbook.note = form.cleaned_data.get("note")
            guestbook.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})


def delete_guestbook(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"guestbook": guestbook})
    else:
        guestbook.delete()
        return redirect("index")
