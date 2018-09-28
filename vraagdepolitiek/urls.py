"""vraagdepolitiek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.static import serve
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from backend.views import QuestionList, QuestionDetail, QuestionCreate, QuestionUpdate, QuestionDelete, QuestionUpvote, UserCreationConfirmView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/q/', QuestionList.as_view(), name='questions'),
    path('api/q/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('api/q/create/', QuestionCreate.as_view(), name='question-create'),
    path('api/q/<int:pk>/edit/', QuestionUpdate.as_view(), name='question-update'),
    path('api/q/<int:pk>/delete/', QuestionDelete.as_view(), name='question-delete'),
    path('api/q/<int:pk>/upvote/', QuestionUpvote.as_view(), name='question-upvote'),

    # API Graphql endpoint
    re_path(r'^api/graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),

    # Admin backend
    path('admin/', admin.site.urls),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/create/<uidb64>/<token>/', UserCreationConfirmView.as_view(), name='user_creation_confirm'),
    path('accounts/create/done/', PasswordResetCompleteView.as_view(), name='user_creation_complete'),

    # Route everything that doesn't match the other paths to frontend
    re_path(r'^_next/(?P<path>.*)$', serve, {'document_root': 'frontend/out/_next'}),
    re_path(r'^', TemplateView.as_view(template_name='index.html')),
]
