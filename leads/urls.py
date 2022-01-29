from django.urls import path
from .views import LeadListView, LeadDetailView,LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('lead_detail/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('lead_create/', LeadCreateView.as_view(), name='lead-create'),
    path('lead_update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('lead_delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
    path('assign-agent/<int:pk>/', AssignAgentView.as_view(), name='assign-agent'),
]
