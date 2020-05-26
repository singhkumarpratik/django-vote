from django.db import models
from users.models import User
from vote.models import VoteModel


class CommentModel(VoteModel, models.Model):
    comment = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
