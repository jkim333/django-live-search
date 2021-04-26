from django.shortcuts import render
from django.views.generic import ListView
from .models import Info
import json

class InfoListView(ListView):
    model = Info
    template_name = 'infos/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Info.objects.values()))
        return context