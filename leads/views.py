from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Lead, Agent
from .forms import LeadForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm


    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class LeadListView(ListView):
    template_name = 'leads/home.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        send_mail(
            subject = "A lead has been created",
            message = "Go to the site to see new lead",
            from_email = "test@test.com",
            recipient_list = ['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

