from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views
from api.views import update_preferences

urlpatterns = [
    path("api/", views.UserList.as_view(), name='users'),
    path("api/<int:pk>/", views.UserDetail.as_view(), name='user-detail'),
    path('api/<int:pk>/update/', update_preferences, name='update-preferences'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
