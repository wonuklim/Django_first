from django.urls import path
from . import views

# 함수, 클래스 연결

app_name = "polls" # 네임스페이스 지정

urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # CBV 방식으로 변경
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

# CRUD rules
    path("create/", views.QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question_update"),
    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question_delete"),
]