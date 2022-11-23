from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist, JobOffer
from news.api.serializers import ArticleSerializers, JournalistSerializers, JobOfferSerializers

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)
    
    def post (self, request):
        print(request.data)
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ArticleDetailCreateAPIView(APIView):
    
    def get_object(self, pk):
        article =get_object_or_404(Article, pk=pk)
        return article
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class JournalistListCreateApiView(APIView):
    def get(self, request):
        
        journalist = Journalist.objects.all()
        serializer = JournalistSerializers(journalist, 
                                           many=True, 
                                           context={'request': request})
        return Response(serializer.data)
    
    def post (self, request):
        print(request.data)
        serializer = JournalistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class JournalistDetailCreateAPIView(APIView):
    
    def get_object(self, pk):
        journalist =get_object_or_404(Journalist, pk=pk)
        return journalist
    
    def get(self, request, pk):
        journalist = self.get_object(pk)
        serializer = JournalistSerializers(journalist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        journalist = self.get_object(pk)
        serializer = JournalistSerializers(journalist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journalist = self.get_object(pk)
        journalist.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class JobOfferListCreateApiView(APIView):
    def get(self, request):
        
        job_offer = JobOffer.objects.all()
        serializer = JobOfferSerializers(job_offer, 
                                           many=True)
        return Response(serializer.data)
    
    def post (self, request):
        print(request.data)
        serializer = JobOfferSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class JobOfferDetailCreateAPIView(APIView):
    
    def get_object(self, pk):
        job_offer =get_object_or_404(JobOffer, pk=pk)
        return job_offer
    
    def get(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializers(job_offer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializers(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk)
        job_offer.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
