from django.shortcuts import render_to_response
from django.template import RequestContext

from webform.forms import MessageForm

from routerq.base import queue


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            queue(backend_name='webform', **form.cleaned_data)
    else:
        form = MessageForm()
    context = {'form': form}
    return render_to_response('webform/send_message.html', context,
                              RequestContext(request))
