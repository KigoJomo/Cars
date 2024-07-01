from django.shortcuts import render
from .models import Car, CarImage
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    return render(request, "index.html")

def local(request):
    #get cars in kenya
    cars = Car.objects.filter(locallyAvailable=True)
    context = {
        'cars': cars,
    }
    return render(request, "cars.html", context)

def imports(request):
    #get cars outside
    cars = Car.objects.filter(locallyAvailable=False)

    context = {
        'cars': cars,
    }
    return render(request, "import.html", context)

def details(request, carId):
    car = Car.objects.get(id=carId)
    context = {
        'car': car,
    }
    return render(request, "details.html", context)


def search(request):
    # Get the query parameter from the request, defaulting to an empty string
    query = request.GET.get('query', '')

    # Perform the search query
    if query:
        # Search for cars by name, make, or model using case-insensitive matching
        cars = Car.objects.filter(
            Q(name__icontains=query) |   # Search by name
            Q(make__icontains=query) |   # Search by make
            Q(model__icontains=query)    # Search by model
        )
        data = [{'name': car.name, 'make': car.make,
                 'model': car.model, 'yearMfct': car.yearMfct, 'trimlevel': car.trimlevel,
                 'image': car.car_images.first().image.url if car.car_images.exists() else None,
                 'price': car.price} for car in cars]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse([], safe=False)

