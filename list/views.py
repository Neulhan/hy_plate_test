from django.shortcuts import render
from plate import models as plate_models

# Create your views here.


def list(request):
    plates = plate_models.Plate.objects.all()
    context = {"plates": plates}
    return render(request, "list/list.html", context)
