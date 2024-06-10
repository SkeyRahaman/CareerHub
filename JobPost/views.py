from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import JobPost

# Create your views here.
def home(request):
    context = {
        'jobs' : JobPost.objects.filter()
    }
    return render(request, 'JobPost/home.html', context)

def job_detail(request,slug):
    try:
        context = {
            'job' : JobPost.objects.get(slug=slug)
        }
        print(JobPost.objects.get(slug=slug))
        return render(request, 'JobPost/job_detail.html', context)
    except:
        return HttpResponseNotFound("Not Found")