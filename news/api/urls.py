from django.urls import path
from news.api.views_apiview import (article_list_create_api_view, article_details_create_api_view)

from news.api.views import (ArticleDetailCreateAPIView,
                            ArticleListCreateAPIView, 
                            JournalistListCreateApiView, 
                            JournalistDetailCreateAPIView, 
                            JobOfferDetailCreateAPIView,
                            JobOfferListCreateApiView)

urlpatterns = [
    path("articles/", article_list_create_api_view, name="article-list"),
    path("articles/<int:pk>", article_details_create_api_view, name="article-detail"),
    
    path("articles/apiviewclass/", ArticleListCreateAPIView.as_view(), name="article-list-class"),
    path("articles/apiviewclass/<int:pk>", ArticleDetailCreateAPIView.as_view(), name="article-detail-class"),

    path("journalist/", JournalistListCreateApiView.as_view(), name="journalist-list-class"),
    path("journalist/<int:pk>", JournalistDetailCreateAPIView.as_view(), name="journalist-detail-class"),

    path("job_offer/", JobOfferListCreateApiView.as_view(), name="job-offer-list-class"),
    path("job_offer/<int:pk>", JobOfferDetailCreateAPIView.as_view(), name="job-offer-detail-class"),
]
