from django.urls import path
from .views import TrashPostView, TrashPostList

urlpatterns = [
    path('input', TrashPostView.as_view()),
    path('list', TrashPostList.as_view()),
]