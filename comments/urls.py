from django.url import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
]