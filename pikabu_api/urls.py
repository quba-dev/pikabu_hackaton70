"""pikabu_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from posts import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title='Pikabushechka')



urlpatterns = [
    path('', include_docs_urls(title='Pikabushechka')),
    path('admin/', admin.site.urls),
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>/', views.PostRetrievDestroy.as_view()),
    path('api/posts/<int:pk>/vote/', views.VoteCreate.as_view()),
    path('api/accounts/', include('user.urls')),
    # path('api/posts/<int:pk>/comment/', views.PostCommentList.as_view()),
    path('api/posts/<int:pk>/comment', views.Comment.as_view()),
]

