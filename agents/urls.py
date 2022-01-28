from unicodedata import name
from django.urls import path
from .views import AgentListView, AgentCreateView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('agent_create/', AgentCreateView.as_view(), name='agent-create'),
]
