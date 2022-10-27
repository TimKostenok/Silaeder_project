from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.main_page, name='main_page'),
  path('new_project/', views.new_project, name='new_project'),
  path('register/', views.register, name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)