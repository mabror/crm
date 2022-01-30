from django.urls import path
from .views import (LeadCategoryUpdateView, 
                    LeadListView, 
                    LeadDetailView,
                    LeadCreateView, 
                    LeadUpdateView, 
                    LeadDeleteView, 
                    AssignAgentView, 
                    CategoryListView,
                    CategoryDetailView,
                    CategoryUpdateView,
                    LeadCategoryUpdateView,
                    CategoryCreateView
                    )

app_name = "leads"


urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('lead_detail/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('lead_create/', LeadCreateView.as_view(), name='lead-create'),
    path('lead_update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('lead_delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
    path('assign-agent/<int:pk>/', AssignAgentView.as_view(), name='assign-agent'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category_detail/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category_update/<int:pk>/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
]
