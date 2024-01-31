from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import like_post, dislike_post

urlpatterns = [path('register', views.UserRegister.as_view(), name="register"),
               path('createprofile',views.CreateProfile.as_view(),name="createprofile"),
               path('home',views.UserHome.as_view(),name="userhome"),
               path('login',views.SignIn.as_view(),name="login"),
               path('logout',views.SignOut.as_view(),name="logout"),
               path('viewprofile',views.ViewProfile.as_view(),name="viewprofile"),
               path('editprofile',views.EditProfile.as_view(),name="editprofile"),
#                path('like/<int:post_id>/', like_post, name='like_post'),
#                path('dislike/<int:post_id>/', dislike_post, name='dislike_post'),
 ]