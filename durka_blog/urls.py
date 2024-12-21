from django.urls import path
from durka_blog.apps import DurkaBlogConfig
from durka_blog.views import (
    PostListView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
)

app_name = DurkaBlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path("durka/", PostListView.as_view(), name="posts_list"),
    path(
        "durka/<int:pk>/",
        PostDetailView.as_view(),
        name="posts_detail",
    ),
    path(
        "durka/create", PostCreateView.as_view(), name="posts_create"
    ),
    path(
        "durka/<int:pk>/update",
        PostUpdateView.as_view(),
        name="posts_update",
    ),
    path(
        "durka/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="posts_delete",
    ),
]
