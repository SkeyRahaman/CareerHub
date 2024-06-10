from django.shortcuts import render,redirect
from .forms import SubscribeModelForm
from django.urls import reverse

# Create your views here.
def subscribe(request):
    email_error = ""
    subscribe_form = SubscribeModelForm()
    if request.POST:
        subscribe_form = SubscribeModelForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
    context = {'form':subscribe_form, "email_error" : email_error}
    return render(request,"Subscribe/subscribe.html", context)

def thank_you(request):
    context = {}
    return render(request,"Subscribe/thank_you.html", context)
