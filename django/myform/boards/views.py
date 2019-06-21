from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from IPython import embed

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

@login_required()
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        #embed()
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)
    comments = board.comment_set.all()
    comment_form = CommentForm()
    context = {
        'board':board,
        'comments':comments,
        'comment_form':comment_form,
        'person':person,
    }
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')
@login_required()
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                # board.title = form.cleaned_data.get('title')
                # board.content = form.cleaned_data.get('content')
                # board.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
    else:
        return redirect('boards:index')
    context = {'form': form, 'board':board}
    return render(request, 'boards/form.html', context)


@login_required
@require_POST
def comments_create(request, board_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    return redirect('boards:detail', board_pk)

@login_required
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('boards:detail', board_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)

@login_required
def like(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)


    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('boards:index')

@login_required()
def follow(request, board_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('boards:detail', board_pk)
