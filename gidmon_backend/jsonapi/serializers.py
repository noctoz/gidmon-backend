from django.contrib.auth.models import User, Group
from rest_framework_json_api import serializers
#from rest_framework_json_api import serializers
from gidmon_backend.jsonapi.models import Beer, Recipe, NewsItem, NewsComment

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		resource_name = "user"
		fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		resource_name = "group"
		fields = ('url', 'name')

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		resource_name = "beers"
		fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		resource_name = "recipes"
		fields = '__all__'
		
class NewsCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsComment
		resource_name = "news_comments"
		fields = '__all__'
		
class NewsItemSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
		'comments': NewsCommentSerializer
	}
	class Meta:
		model = NewsItem
		resource_name = "news_items"
		fields = ('title', 'content', 'author', 'comments')
