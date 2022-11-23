from rest_framework import serializers
from news.models import Article,Journalist,JobOffer
from datetime import datetime
from django.utils.timesince import timesince

# Model serializers

class ArticleSerializers (serializers.ModelSerializer):
    
    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalistSerializers(read_only=True)
    
    class Meta:
        model = Article
        # we want all the fields of our model
        # fields = "__all__" 
        
        # specific fields
        # fields = ("title", "desciption", "body")
        exclude = ("id",) #exclude fields
    
    def get_time_since_publication(self, object):
        
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta
    
    # Object Validation
    # Validation using multiple fields (object)
    def validate(self, data):
        """Check that description"""
        
        if data["title"] == data["description"]:
            raise serializers.ValidationError("title and description must be different from one another")
        return data
    
    # Fields Validation
    # Validation perform on specific fields
    def validate_title(self, value):
        
        if len(value) < 60:
            raise serializers.ValidationError("title must be at least 60 characters long")
        return value
    
class JournalistSerializers(serializers.ModelSerializer):
    
    articles= serializers.HyperlinkedRelatedField(many=True,
                                                  read_only=True, 
                                                  view_name="article-detail-class")
    
    class Meta:
        model = Journalist
        fields = "__all__" 
        
class JobOfferSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = JobOffer
        fields = "__all__" 

