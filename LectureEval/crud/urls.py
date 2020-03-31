from django.urls import path
from . import views

urlpatterns = [
    path('<int:lect_id>/', views.EvalList, name = "evallist"),
    path('<int:lect_id>/write/', views.write, name = "write"),
    path('create', views.create, name = "create"),
    path('detail/<int:eval_id>/', views.detail, name = "detail"),
    path('<int:eval_id>/update', views.update, name = "update"),
    path('<int:eval_id>/delete', views.delete, name = "delete"),
    path('addLecture/', views.addLecture, name = "addLecture"),
    path('<int:lect_id>/evalpost/', views.evalpost, name = "evalpost"),
]
