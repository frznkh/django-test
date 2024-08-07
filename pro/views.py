from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound


# Create your views here.
days={
    'saterday': 'this is saterday',
    'sunday': 'this is sunday',
    'monday': 'this is monday',
    'tuesday': 'this is tuesday',
    'wensday': 'this is wensday',
    'tursday': 'this is tursday',
    'friday': 'this is friday',
}
def dainamic_days(request,day , descreption):
    data_day=days.get(day)
    if data_day is None:
        return HttpResponse(f'day is {day} and date is : {data_day} ')

    return HttpResponseNotFound (' not found ')