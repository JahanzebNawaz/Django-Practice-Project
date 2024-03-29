from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailsView.as_view(), name='article_page'),
    path('article/new/', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/update/<int:pk>/edit', views.AticleUpdateView.as_view(), name='article_edit'),
    path('article/update/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),

]
