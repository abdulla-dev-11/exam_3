from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.IndexlistView.as_view(), name='home'),
    path('about/', views.AboutlistView.as_view(), name='about'),
    path('detail/<int:pk>', views.post_detail, name='post_detail'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('email/', views.EmailView.as_view(), name='email'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.policy_view, name='policy')
]