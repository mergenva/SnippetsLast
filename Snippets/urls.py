from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from MainApp import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index_page, name='home'),
    path('accounts/login', views.index_page, name='home'),
    path('snippet/add', views.add_snippet_page, name='snippet_add'),
    path('comment/add', views.add_comment, name='comment_add'),
    path('snippets/list', views.snippets_page, name='snippets'),
    path('snippets/my', views.snippets_my, name='my_snippets'),
    path('snippet/<int:snippet_id>', views.snippet_page, name='snippet'),
    path('snippet/delete/<int:snippet_id>', views.snippet_delete, name='snippet_delete'),
    path('snippet/edit/<int:snippet_id>', views.snippet_edit, name='snippet_edit'),
    path('auth/login', views.login_page, name='login'),
    path('auth/logout', views.logout_page, name='logout'),
    path('auth/registry', views.create_user, name='registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
