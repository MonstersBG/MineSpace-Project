from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ForumCreationForm, CommentForm
from .models import Forum, Comment, Upvote, Favorites
from django.views import generic as views


# Create your views here.

def home(request):
    forums = Forum.objects.all()

    context = {
        "forums": forums
    }

    return render(request, 'home-page.html', context)


@login_required
def create_forum(request):
    if request.method == "POST":
        form = ForumCreationForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.user = request.user
            new_forum.save()
            return redirect('home')
    else:
        form = ForumCreationForm()

    context = {
        "form": form
    }

    return render(request, 'forum/forum-creation.html', context)


class ForumDetailView(views.DetailView):
    model = Forum
    template_name = 'forum/forum-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["is_owner"] = self.object.user == self.request.user
        return context


@login_required
def add_comment(request, pk):
    forum = Forum.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.to_forum = forum
            new_comment.save()
            return redirect('details_forum', pk=pk)

    return redirect('details_forum', pk=pk)


@login_required
def like_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    context = {
        "to_comment": comment,
        "user": request.user,
    }

    upvote_object = Upvote.objects.filter(**context).first()

    if upvote_object:
        upvote_object.delete()
    else:
        new_upvote_object = Upvote(**context)
        new_upvote_object.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{pk}")


@login_required
def favorite_forum(request, pk):
    forum = Forum.objects.get(pk=pk)

    context = {
        "to_forum": forum,
        "user": request.user,
    }

    favorite_object = Favorites.objects.filter(**context).first()

    if favorite_object:
        favorite_object.delete()
    else:
        new_favorite_object = Favorites(**context)
        new_favorite_object.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def edit_forum(request, pk):
    forum = Forum.objects.filter(pk=pk).first()

    if request.method == "POST":
        form = ForumCreationForm(request.POST, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('details_forum', pk=pk)
    else:
        form = ForumCreationForm(instance=forum)

    is_owner = forum.user == request.user

    context = {
        "form": form,
        "forum": forum,
        "is_owner": is_owner
    }

    return render(request, 'forum/forum_edit.html', context)


# def search_forums(request):
#     query = request.GET.get('q')
#
#     if query:
#         forums = Forum.objects.filter(title__icontains=query)
#     else:
#         forums = Forum.objects.none()
#
#     context = {
#         'forums': forums,
#         'query': query,
#     }
#     return render(request, 'forum/search_results.html', context)

def search_forums(request):
    query = request.GET.get('q')

    if query:
        forums = Forum.objects.filter(title__icontains=query)
    else:
        forums = Forum.objects.order_by('title')

    context = {
        'forums': forums,
        'query': query,
    }
    return render(request, 'forum/search_results.html', context)


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    forum_id = comment.to_forum_id
    if comment.user == request.user:
        comment.delete()
        return redirect('details_forum', pk=forum_id)
    else:
        context = {
            'message': "You don't have permission to delete this comment."
        }
        return render(request, 'forum/permission_denied.html', context)
