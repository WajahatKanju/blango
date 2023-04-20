from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token as rest_auth_token
from blog.api.views import PostList, PostDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns += [
  path('auth/', include('rest_framework.urls')),
  path('token-auth/', rest_auth_token)
]