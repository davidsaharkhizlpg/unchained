# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from polls.models import Poll
from django.template import Context, loader

# you can define these any way you like, they are associated with an url pattern from /root/urls.py

#main page (/polls/)
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
	
#handling a specific poll (example: /polls/23)	
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})
def results(request, poll_id):
    return HttpResponse("<b>You're</b> looking at poll %s." % poll_id)
def vote(request, poll_id):
    return HttpResponse("")
