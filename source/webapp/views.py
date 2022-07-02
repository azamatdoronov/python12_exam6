from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Guestbook, STATUS_CHOICES


def index_view(request):
    guestbooks = Guestbook.objects.order_by("-update_nt")
    context = {"guestbooks": guestbooks}
    return render(request, "index.html", context)






