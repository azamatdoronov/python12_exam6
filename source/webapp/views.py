from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestbookForm
from webapp.models import Guestbook, STATUS_CHOICES


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




