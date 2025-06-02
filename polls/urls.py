from django.urls import path
from . import views

# 함수, 클래스 연결

app_name = "polls" # 네임스페이스 지정

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]