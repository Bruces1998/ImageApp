from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('image/',views.ImageListView.as_view(),name='imagelist'),
    path('file/',views.FileListView.as_view(),name='filelist'),
    path('addimage/',views.AddImage.as_view(),name='addimage'),
    path('addfile/',views.AddFile.as_view(),name='addfile'),
    path('timeline/',views.Timeline.as_view(),name='timeline')
    # path('file/',views.FileListView.as_view(),name='filelist')

]
