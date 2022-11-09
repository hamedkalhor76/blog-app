from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.post_list, name='index'),
    path('post-list/<str:tag_slug>/', views.post_list, name='index_tag'),
    path('post-detail/<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_detail, name='post_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
]