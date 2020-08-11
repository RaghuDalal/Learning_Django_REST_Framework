from django.shortcuts import render
from django.http import JsonResponse

from DRF.models import Employee


def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'salary': 1000000
    }

    data = Employee.objects.all();
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)
