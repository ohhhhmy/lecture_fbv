
from django.contrib import admin
from django.urls import path, include
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.LectureList, name = "lectureList"),
    path('', include('crud.urls')),
    path('accounts/', include('login.urls')),
]

