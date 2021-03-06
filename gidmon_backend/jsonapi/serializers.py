from django.contrib.auth.models import User, Group, Permission
from rest_framework_json_api import serializers
#from rest_framework_json_api import serializers
from gidmon_backend.jsonapi import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		resource_name = "user"
		fields = ('url', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_superuser', 'user_permissions', 'profile')
		read_only_fields = ('user_permissions', 'profile',)

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		resource_name = "group"
		fields = ('url', 'name')

class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		resource_name = "permission"
		fields = ('name', 'codename')

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Profile
		resource_name = "profiles"
		fields = '__all__'
		read_only_fields = ('user', 'picture')

class BrewingSystemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BrewingSystem
		resource_name = "brewing_systems"
		fields = '__all__'

class BoilIngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoilIngredient
		resource_name = "boil_ingredients"
		fields = '__all__'

class MashIngredientTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MashIngredientType
		resource_name = "mash_ingredient_types"
		fields = '__all__'

class MashIngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MashIngredient
		resource_name = "mash_ingredients"
		fields = '__all__'

class YeastSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Yeast
		resource_name = "yeasts"
		fields = '__all__'

class BeerTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerType
		resource_name = "beer_types"
		fields = '__all__'

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Beer
		resource_name = "beers"
		fields = '__all__'

class PitchTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.PitchType
		resource_name = "pitch_types"
		fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
	included_serializers = {
		'yeast': YeastSerializer,
		'pitch_type': PitchTypeSerializer,
	}
	class Meta:
		model = models.Recipe
		resource_name = "recipes"
		fields = ('beer', 'creator', 'mashing_temp', 'mashing_time', 'mash_out_temp', 'mash_out_time', 'sparge_count', 'sparge_water_temp', 'sparge_time',
			'conversion_efficiency', 'pre_boil_volume', 'post_boil_volume', 'fermentation_volume', 'final_volume', 'boil_time', 'total_malt_weight', 'primary_fermentation_temp', 
			'primary_fermentation_time', 'yeast', 'yeast_amount', 'pitch_type',
			'boil_entries', 'mash_entries', 'sessions', 'creators')
		read_only_fields = ('creator', 'boil_entries', 'mash_entries', 'sessions', 'creators')

class RecipeCreatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RecipeCreator
		resource_name = "recipe_creators"
		fields = ('creator', 'recipe')
		read_only_fields = ('creator', 'recipe')

class BrewingSessionCommentSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
	}
	class Meta:
		model = models.BrewingSessionComment
		resource_name = "brewing_session_comments"
		fields = ('content', 'children', 'author', 'brewing_session')
		read_only_fields = ('children', 'author')

class BrewingSessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BrewingSession
		resource_name = "brewing_sessions"
		fields = ('date', 'recipe', 'brewing_system', 'strike_water_volume', 'strike_water_temp', 'sparge_water_volume', 'sparge_water_temp', 'pre_boil_volume', 
		'measured_pre_boil_volume', 'post_boil_volume', 'measured_post_boil_volume', 'fermentation_volume', 'measured_fermentation_volume', 'final_volume', 'measured_final_volume', 'boil_time', 'measured_first_wort_sg', 
		'measured_first_sparge_sg', 'measured_pre_boil_sg', 'measured_og', 'measured_fg', 'wort_settle_time', 'yeast_used', 'sugar_used', 'boil_entries', 'mash_entries', 'comments', 'brewers')
		read_only_fields = ('boil_entries', 'mash_entries', 'comments', 'brewers')

class SessionBrewerSerializer(serializers.ModelSerializer):
	included_serializers = {
		'brewer': UserSerializer,
	}
	class Meta:
		model = models.SessionBrewer
		resource_name = "session_brewers"
		fields = '__all__'
		read_only_fields = ('brewer',)

class BeerBatchSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerBatch
		resource_name = "beer_batches"
		fields = '__all__'

class BoilRecipeEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoilRecipeEntry
		resource_name = "boil_recipe_entries"
		fields = '__all__'

class MashRecipeEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MashRecipeEntry
		resource_name = "mash_recipe_entries"
		fields = '__all__'

class BoilSessionEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoilSessionEntry
		resource_name = "boil_session_entries"
		fields = '__all__'

class MashSessionEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MashSessionEntry
		resource_name = "mash_session_entries"
		fields = '__all__'

class NewsCommentSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
	}
	class Meta:
		model = models.NewsComment
		resource_name = "news_comments"
		fields = ('content', 'children', 'author', 'news_item')
		read_only_fields = ('children', 'author')
		
class NewsItemSerializer(serializers.ModelSerializer):
	included_serializers = {
		'author': UserSerializer,
		'comments': NewsCommentSerializer
	}
	class Meta:
		model = models.NewsItem
		resource_name = "news_items"
		fields = ('title', 'preamble', 'content', 'created', 'author', 'comments')
		read_only_fields = ('author', 'comments')
