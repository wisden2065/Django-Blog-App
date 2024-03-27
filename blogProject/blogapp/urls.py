

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name='blogapp'

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('', views.post_list, name="post_list"),
    path('admin/', admin.site.urls),

    path('logout/', auth_view.LogoutView.as_view(), name ='logout'),
    path('password-change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('<int:id>/', views.post_view, name ='post-detail'),
    path('createpost/', views.CreatAPost, name='createapost'),

]