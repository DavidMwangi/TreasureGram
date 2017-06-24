from django.shortcuts import render
from .models import Treasure

# Create your views here.

def index(request):

    """"

        Query set fetches all treasure objects from our models
        Treasures are passed to index.html template to be rendered

    """

    treasures = Treasure.objects.all()
    return render(request, 'main_app/index.html', {'treasures':treasures})

def detail(request, treasure_id):

    """

    :param request:

    :param treasure_id: Receives a number value from url dispatcher in the form localhost/value
     Assigns value to parameter treasure_id. Using the query set below, the treasure with the
     treasure_id is retrieved from our model and assigned variable treasure.

    :return: Rendered detail.html template for the treasure retrieved

    """

    treasure = Treasure.objects.get(id=treasure_id)

    return render(request, 'main_app/detail.html', {'treasure':treasure})


"""
#DYNAMIC DATA

class Treasure():

    def __init__(self, name, value, material,location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [

    Treasure('Gold Nugget', 500.00, 'gold', 'Curly Creek NM', ""),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Fall, CO", ""),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', ""),
]

"""