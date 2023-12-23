from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView, CreateView, UpdateView
from Main.models import Details
# from Main.forms import LeadModelForm

def landingpage(request):
    return render (request, "landingpage.html")


# class LeadCreateView(CreateView):
#    template_name="leads/lead_create.html"
#    form_class = LeadModelForm
   
#    def get_success_url(self):
#       return "/leads"
   