from django.conf import settings
from django.shortcuts import render, get_object_or_404

# Create your views here.
from plate.models import Plate


def plate_list(request):
    plates = Plate.objects.all()
    context = {"plates": plates}
    return render(request, "plate/list.html", context)


def detail(request, pk):
    plate = get_object_or_404(Plate, pk=pk)

    context = {
        "plate": plate,
        "kakao_js": settings.KAKAO_API_KEY_JAVASCRIPT
    }
    return render(request, "plate/detail.html", context)
