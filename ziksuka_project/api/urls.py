from django.urls import path,include
from .views import BlogDetail,BlogList,UserListView
urlpatterns = [
    path('blogs/',BlogList.as_view()),
    path('blogs/<int:pk>',BlogDetail.as_view()),
    path('users/',UserListView.as_view()),
]
