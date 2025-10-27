from django.urls import path
from .views import home, create_user, user_view
urlpatterns = [
    path('home/', home),
    path('create/', create_user),
    path('view/', user_view)
]
