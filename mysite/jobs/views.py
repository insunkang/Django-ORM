from django.shortcuts import render
from jobs.models import Person
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request,'jobs/index.html')

def past_life(request,person_pk):
    job = Job.objects.get(pk=person_pk)
    context = {
        'job' = job 
    }
    return render(request,'jobs:past_life')