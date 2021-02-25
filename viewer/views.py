from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import os
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'viewer/index.html')

def pdf_view(request, order_type, page_number):
    try:
        filename = page_number + ".pdf"
        filepath = os.path.join( settings.MEDIA_ROOT, "BSES", order_type, filename)
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        messages.error(request, "Page Number " + page_number + " doesn't exists.")
        return HttpResponseRedirect(reverse("viewer:index"))
