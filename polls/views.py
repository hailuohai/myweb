from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ClubChartView(TemplateView):
    template_name = 'clubs/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Index(TemplateView):
    template_name = 'clubs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

