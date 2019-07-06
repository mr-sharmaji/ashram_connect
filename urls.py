from django.urls import path,include
from . import views

urlpatterns = [
#<int:album_id>/
#/(?P<pk>\d+)
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('profile/',views.profile_user,name='profile'),
    path('mypost/',views.UserListView.as_view(),name='mypost'),
    #path('profile',views.UserProfileView.as_view(),name='profile'),
    path('settings/',views.user_settings,name='settings'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',views.PostDeleteView.as_view(),name='post_remove'),
    path('post/drafts/',views.DraftListView.as_view(),name='post_draft'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    #path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    #path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
]
