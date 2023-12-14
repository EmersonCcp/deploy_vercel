from django.urls import path, include
from . import views    # --- (1)
 
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('edit/<int:article_id>', views.edit, name='edit'), 
    path('delete/<int:article_id>', views.delete, name='delete'), 
    path('__debug__/', include('debug_toolbar.urls')),
]