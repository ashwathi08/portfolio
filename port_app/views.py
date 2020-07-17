from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import About,Skills
# Create your views here.
class IndexView(TemplateView):
    template_name = 'port_app/index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['about']=About.objects.first()
        context['skill']=Skills.objects.all()
        return context
