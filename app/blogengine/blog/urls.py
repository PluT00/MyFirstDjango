from django.urls import path

from .views import *

urlpatterns = [
    path ('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetails.as_view(), name='post_details_url'),
    path('post/<str:slug>/edit', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/create', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetails.as_view(), name='tag_details_url'),
    path('tags/<str:slug>/edit/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]
