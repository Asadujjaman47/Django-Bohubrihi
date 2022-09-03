from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album

# Create your views here.


def index(request):
    # SELECT * FROM Musician ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'text_1': 'This is a list of Musician',
        'musician': musician_list
    }
    return render(request, 'first_app/index.html', context=diction)
