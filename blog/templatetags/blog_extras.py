from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django import template

from blog.models import Post


user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    return user_model
  
  if author == current_user:
    return format_html('<strong>Me</strong>')

  if author.first_name and author.last_name and author.email:
    return mark_safe(f'<a href="mailto:{escape(author.email)}">{escape(author.first_name)} {escape(author.last_name)} </a>')

  if author.first_name and author.last_name:
    return f'{author.first_name} {author.last_name}'
  
  if author.email:
    return mark_safe(f'<a href="mailto:{escape(author.email)}">{escape(author.username)} </a>')

  return author.username

@register.simple_tag
def row(extra_classes=''):
  return format_html('<div class="row {} ">', extra_classes)

@register.simple_tag
def endrow():
  return format_html('</div>')


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  post = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": post}
