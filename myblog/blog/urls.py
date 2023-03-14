from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexPage.as_view()),
    path('<int:pk>/', views.PublicationPage.as_view()),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('<int:pk>/add_like', views.AddLike.as_view(), name='add_like'),
    path('<int:pk>/del_like', views.DelLike.as_view(), name='del_like'),
]
