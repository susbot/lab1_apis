from django.urls import path
from apis import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]