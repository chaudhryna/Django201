from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path('update_profile/', views.update_profile, name='update_profile'),
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
]