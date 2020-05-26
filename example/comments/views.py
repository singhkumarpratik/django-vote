from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from .models import CommentModel


class CommentView(ListView):
    model = CommentModel


def comment_vote(request, comment_id):
    comment = CommentModel.objects.get(pk=comment_id)
    print(comment_id)
    # 0 is upvote, 1 is downvote
    user_votes_up = comment.votes.user_ids(0)
    user_votes_down = comment.votes.user_ids(1)
    check = {"user_id": request.user.id}
    # check if user is logged in. If not redirect to login page
    if request.user.is_authenticated:
        if request.is_ajax and request.method == "GET":
            # get the value passed from the form
            if request.GET.get("up"):
                # check if user has already upvoted, if yes, remove user's upvote
                if check in user_votes_up.values("user_id"):
                    comment.votes.delete(request.user.id)
                # else upvote the comment
                else:
                    comment.votes.up(request.user.id)
            if request.GET.get("down"):
                # check if user has already downvoted, if yes, remove user's downvote
                if check in user_votes_down.values("user_id"):
                    comment.votes.delete(request.user.id)
                # else downvote the comment
                else:
                    comment.votes.down(request.user.id)
            if request.GET.get("status"):
                has_upvoted = comment.votes.exists(request.user.id, action=0)
                has_downvoted = comment.votes.exists(request.user.id, action=1)
                return JsonResponse(
                    {"has_upvoted": has_upvoted, "has_downvoted": has_downvoted,}
                )
            comment = CommentModel.objects.get(pk=comment_id)
            # print(comment.votes.exists(request.user.id, action=0))
            has_upvoted = comment.votes.exists(request.user.id, action=0)
            has_downvoted = comment.votes.exists(request.user.id, action=1)
            return JsonResponse(
                {
                    "valid": True,
                    "data": {
                        # "upvote": comment.num_vote_up,
                        # "downvote": comment.num_vote_down,
                        "score": comment.vote_score,
                        "has_upvoted": has_upvoted,
                        "has_downvoted": has_downvoted,
                    },
                },
                status=200,
            )
            # return redirect("home:comment")
    else:
        # if user is not logged in
        return redirect("users:login")
