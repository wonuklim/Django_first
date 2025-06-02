from django.contrib import admin
from django.urls import path, include

# 라우터 연결

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")),
]
