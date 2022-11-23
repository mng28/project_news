from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Article
from news.api.serializers import ArticleSerializers

@api_view(["GET", "POST"])
def article_list_create_api_view(request):
    
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print(request.data)
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def article_details_create_api_view(request, pk):
    
    try:
        articles = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({
            "error":{
                "code": 404,
                "message": "Article not found"
            }
        }, status = status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = ArticleSerializers(articles)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializers(articles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        articles.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)