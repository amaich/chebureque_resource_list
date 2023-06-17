from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main(request):
    resources = ResourceModel.objects.all()
    return render(request, 'resource_list/start_page.html', {'resources': resources})


# Create your views here.
