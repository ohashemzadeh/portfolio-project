from django.shortcuts import render

# Create your views here.
from .models import Job


def home(request):
    template_name = 'jobs/home.html'

    jobs = Job.objects.all()

    context = {'jobs' : jobs}
    return render(request, template_name, context)