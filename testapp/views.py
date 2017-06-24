from django.shortcuts import render
from main_app.models import Treasure


def test(request):

    treasures = Treasure.objects.all()

    return render(request, 'testapp/test.html', {'treasures':treasures})
