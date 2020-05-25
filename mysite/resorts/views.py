from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import ResortName
def index(request):
    latest_resorts = ResortName.objects.order_by('-booking_date')[:5]
    return render(request, 'resorts/index.html', {
        'latest_resorts':latest_resorts
    })

def detail(request, resort_id):
    resort = get_object_or_404(ResortName, pk = resort_id)
    return render(request, 'resorts/detail.html', {'resort':resort})

def results(request, resort_id):
    resort = get_object_or_404(ResortName, pk=resort_id)
    return render(request, 'resorts/results.html', {'resort':resort})

def dish(request, resort_id):
    return HttpResponse('Dish of the resort: %s' % resort_id)

def resortReview(request, resort_id):
    resort = get_object_or_404(ResortName, pk=resort_id)
    try:
        selected_resortreview = resort.resortreview_set.get(pk = request.POST['resortreview'])
    except:
        return render(request, 'resorts/detail.html', {'resort':resort, 'error_message':'please add resort review'})
    else:
        selected_resortreview = ''
        selected_resortreview.save()

        return HttpResponseRedirect(reverse('resorts/results.html', args=(resort_id,)))


