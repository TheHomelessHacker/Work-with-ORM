from django.http import Http404
from django.shortcuts import render

from main.models import Car, Client, Sale

def greeting(request):
    template_name = 'main/greetings.html'
    return render(request, template_name)


def cars_list_view(request):
    template_name = 'main/list.html'
    car_list = Car.objects.all()
    
    context = {
        'car_list': car_list
    }

    return render(request, template_name, context)


def car_details_view(request, car_id):
    try:
        template_name = 'main/details.html'
        car = Car.objects.get(id=car_id)

        context = {
            'car': car
        }
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')

def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        car = Car.objects.get(id=car_id)
        cliet_list = Sale.objects.filter(car=car).select_related('client')
        context = {
            'car': car,
            'sales': cliet_list
        }
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
