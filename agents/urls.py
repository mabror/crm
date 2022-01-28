from unicodedata import name
from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('agent_create/', AgentCreateView.as_view(), name='agent-create'),
    path('agent_detail/<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agent_update/<int:pk>/', AgentUpdateView.as_view(), name='agent-update'),
    path('agent_delete/<int:pk>/', AgentDeleteView.as_view(), name='agent-delete'),
]
