from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import TestForm


# Create your views here.
def index(request):
    template = loader.get_template('carbon/index2.html')
    context = {}
    # return render(request, 'carbon/index.html', context)
    return HttpResponse(template.render(context, request))

def index3(request):
    template = loader.get_template('carbon/index3.html')
    context = {}
    # return render(request, 'carbon/index.html', context)
    return HttpResponse(template.render(context, request))

class DefaultFormByFieldView(FormView):
    template_name = "carbon/form_by_field.html"
    form_class = TestForm
