from django.conf.urls import url,include
from blogapp.views import IndexView, AboutMe, ListArticle, Contact, Article

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^/(?P<id>[0-9]+)/?', Article.as_view(), name='article_detail'),
    url(r'^aboutme/?', AboutMe.as_view(), name='aboutme'),
    url(r'^listarticle/$', ListArticle.as_view(), name='list_article'),
    url(r'^contact/?', Contact.as_view(), name='contact'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
