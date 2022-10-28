from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.main_page, name='main_page'),
  path('new_project/', views.new_project, name='new_project'),
  path('register/', views.register, name='register'),
  path('login/', views.login_view, name='login_view'),
  path('logout/', views.logout_view, name='logout_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)