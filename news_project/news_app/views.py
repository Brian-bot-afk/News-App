from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import JournalistSerializer
# Create your views here.

class JournalistView(APIView):
   def get (self, request):
       journalists = Journalist.objects.all()
       serializer = JournalistSerializer(journalists, many=True)
       return Response({"journalists":serializer.data})
from .serializers import JournalistSerializer, ArticleSerializer
class ArticleView(APIView):
   def get (self, request):
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return Response({"articles":serializer.data})
# Create your views here.
   def post(self, request):
       article = request.data.get('article')

       serializer = ArticleSerializer(data=article)
       if serializer.is_valid(raise_exception=True):
           saved_article = serializer.save()
       return Response({"success": "Article '{}' created successfully".format(saved_article.title)})
class ArticleDetailView(APIView):   
   def put(self, request, pk):
       saved_article = get_object_or_404(Article.objects.all(), pk=pk)
       serializer = ArticleSerializer(instance=saved_article, data=request.data, partial=True)
       if serializer.is_valid(raise_exception=True):
           article_saved = serializer.save()
       return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

   def delete(self, request, pk):
       # Get object with this pk
       article = get_object_or_404(Article.objects.all(), pk=pk)
       article.delete()
       return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
 