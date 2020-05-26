from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import CommentView, comment_vote

app_name = "home"
urlpatterns = [
    path("", CommentView.as_view(), name="comment"),
    path("<int:comment_id>/vote", comment_vote, name="comment-vote"),
]
