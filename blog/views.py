import logging 

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from blog.models import Post
from .forms import CommentForm

logger = logging.getLogger(__name__)


@cache_page(300)
@vary_on_headers('Cookie')
def index(request):
  posts = (Post.objects.filter(published_at__lte=timezone.now()).select_related('author').select_related('author'))
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html", {"posts": posts})

def post_detial(request, slug):
  
  post = get_object_or_404(Post, slug=slug)
  
  if request.method == 'POST':
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
      comment =comment_form.save(commit=False)
      comment.content_object = post
      comment.creator = request.user
      comment.save()
      logger.info("Created comment on Post %d for user %s", post.pk, request.user)
      return redirect(request.path_info)
    else:
      comment_form = CommentForm()
  else:
    comment_form = CommentForm()
  
  context = {"post": post, "comment_form": comment_form}

  return render(request, "blog/post-detail.html", context)

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])