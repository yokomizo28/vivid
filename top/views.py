from django.shortcuts import render
from .models import Content
from django.views import generic
from django.http import HttpResponse,Http404

class IndexView(generic.TemplateView):
    template_name = 'top/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_list'] = Content.objects.filter(categories=1).order_by('?')
        context['netflix'] = Content.objects.filter(services=1).order_by('?')[:10]
        context['prime_video'] = Content.objects.filter(services=2).order_by('?')[:10]
        context['u_next'] = Content.objects.filter(services=3).order_by('?')[:10]
        context['hulu'] = Content.objects.filter(services=4).order_by('?')[:10]
        return context
