from django.db import models
from django.contrib.auth.models import User
from decimal import *

class BrewingSystem(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	evaporation_rate = models.DecimalField(u"evaporation rate in l/hour", max_digits=4, decimal_places=1, default=0)
	transfer_loss = models.DecimalField(u"loss due to transfer to boiler", max_digits=4, decimal_places=1, default=0)
	boiler_dead_space = models.DecimalField(u"dead space when transfering to fermentor", max_digits=4, decimal_places=1, default=0)
	conversion_efficiency = models.IntegerField(u"conversion efficiency (%)", default=100)
	lauter_efficiency = models.IntegerField(u"lautering efficienct (%)", default=100)

class BoilIngredient(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	alpha = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	INGREDIENT_TYPES = (
		(u'cones', u'Hops Cones'),
		(u'pellets', u'Hops Pellets'),
		(u'other', u'Other'),
	)
	ingredient_type = models.CharField(max_length=10, choices=INGREDIENT_TYPES, default='cones')

	def __str__(self):
		return u'%s, %f.2%%' % (self.name, self.alpha)

class MashIngredientType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	extract_potential = models.IntegerField(default=0)
	is_malt = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class MashIngredient(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	ebc = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	dbfg = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	mc = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	ingredient_type = models.ForeignKey(MashIngredientType)

	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "mash_ingredients"

class Yeast(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	fermentation_temp_min = models.IntegerField(default=0)
	fermentation_temp_max = models.IntegerField(default=0)
	ideal_temp_min = models.IntegerField(default=0)
	ideal_temp_max = models.IntegerField(default=0)
	alcohol_tolerance = models.IntegerField(default=0)
	YEAST_TYPES = (
		(u'dry', u'Dry'),
		(u'liquid', u'Liquid'),
	)
	yeast_type = models.CharField(max_length=10, choices=YEAST_TYPES, default='dry')
	attenuation = models.DecimalField(max_digits=3, decimal_places=1, default=0)
	cell_concentration = models.DecimalField(u"billion cells/g", max_digits=5, decimal_places=3, default=0)
	FLOCCULATION_TYPES = (
		(u'low', u'Low'),
		(u'medium', u'Medium'),
		(u'high', u'High'),
	)
	flocculation = models.CharField(max_length=10, choices=FLOCCULATION_TYPES, default='medium')
	
	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "yeasts"

class BeerType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return self.name

class Beer(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	image_name = models.CharField(max_length=30, default='dummy.gif')
	beer_type = models.ForeignKey(BeerType, related_name='beers_of_type')

	def __str__(self):
		return self.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "beers"

class Recipe(models.Model):
	beer = models.OneToOneField(Beer, related_name='recipe')
	creator = models.ForeignKey(User)
	mashing_temp = models.IntegerField(u"mashing temperature", default=65)
	mashing_time = models.IntegerField(u"mashing time", default=60)
	mash_out_temp = models.IntegerField(u"mash out temperature", default=75)
	mash_out_time = models.IntegerField(u"mash out time", default=20)
	sparge_count = models.IntegerField(u"number of sparges", default=1)
	sparge_water_temp = models.IntegerField(u"sparge water temperature", default=73)
	pre_boil_volume = models.DecimalField(u"pre boil volume", max_digits=4, decimal_places=2, default=20)
	boil_time = models.IntegerField(u"time to boil in minutes", default=60)
	total_malt_weight = models.DecimalField(u"total malt weight", max_digits=4, decimal_places=1, default=5)
	primary_fermentation_temp = models.IntegerField(u"primary fermentation temp (C)", default=18)
	primary_fermentation_time = models.IntegerField(u"primary fermentation time (days)", default=14)
	yeast = models.ForeignKey(Yeast)
	yeast_amount = models.DecimalField(u"amount of yeast (g)", max_digits=4, decimal_places=1, default=0)
	TARGET_PITCH_TYPE = (
		(Decimal(0.35), u'Manufacturer'),
		(Decimal(0.5), u'Manufacturer 1.060+'),
		(Decimal(0.75), u'Ale'),
		(Decimal(1.0), u'Ale 1.060+'),
		(Decimal(1.5), u'Lager'),
		(Decimal(2.0), u'Lager 1.060+'),
	)
	target_pitch_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.75, choices=TARGET_PITCH_TYPE)

	def __str__(self):
		return 'Recipe: %s' % self.beer.name

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "recipes"

class BrewingSession(models.Model):
	date = models.DateTimeField();
	recipe = models.ForeignKey(Recipe, related_name='sessions');
	brewing_system = models.ForeignKey(BrewingSystem)
	strike_water_temp = models.IntegerField(u"measured strike water temperature", default=0)
	strike_water_volume = models.IntegerField(u"measured strike water volume", default=0)
	sparge_water_temp = models.IntegerField(u"measured sparge water temperature", default=0)
	sparge_water_volume = models.IntegerField(u"measured sparge water volume", default=0)
	pre_boil_volume = models.DecimalField(u"measured pre boil volume", max_digits=4, decimal_places=2, default=0)
	post_boil_volume = models.DecimalField(u"measured post boil volume", max_digits=4, decimal_places=2, default=0)
	fermentation_volume = models.DecimalField(u"volume in fermentation vessel", max_digits=4, decimal_places=2, default=0)
	wort_rest_time = models.IntegerField(u"time to rest the wort", default=0)
	yeast_amount = models.DecimalField(u"actual amount of yeast", max_digits=4, decimal_places=2, default=0)

	def __str__(self):
		return 'Session: %s' % self.beer.name

class BeerBatch(models.Model):
	name = models.CharField(max_length=100)
	abv = models.IntegerField(default=0)
	untappd_url = models.CharField(max_length=100)
	session = models.OneToOneField(BrewingSession, related_name='beer_batch');

	def __str__(self):
		return u'Beer Batch: %s' % (self.name)

class BoilRecipeEntry(models.Model):
	recipe = models.ForeignKey(Recipe, related_name='boil_entries')
	ingredient = models.ForeignKey(BoilIngredient)
	amount = models.IntegerField(u'amount in grams', default=0)
	add_time = models.IntegerField(u'time to add from start of boil', default=0)

	def __str__(self):
		return u'Recipe Entry: %s, %s' % (self.recipe.beer.name, self.ingredient.name)

class MashRecipeEntry(models.Model):
	recipe = models.ForeignKey(Recipe, related_name='mash_entries')
	ingredient = models.ForeignKey(MashIngredient)
	amount = models.DecimalField(u'amount of malt in %', max_digits=4, decimal_places=1, default=0)
	
	def __str__(self):
		return u'Recipe Entry: %s, %s' % (self.recipe.beer.name, self.ingredient.name)
		
class NewsItem(models.Model):
	title = models.CharField(max_length=100)
	preamble = models.TextField()
	content = models.TextField()
	created = models.DateTimeField()
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "news_items"
		
class NewsComment(models.Model):
	news_item = models.ForeignKey(NewsItem, related_name='comments')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True) 
	content = models.TextField()
	author = models.ForeignKey(User)

	def __str__(self):
		return 'Comment on: %s' % self.news_item.title

	# Needed to serialize relations properly
	class JSONAPIMeta:
		resource_name = "news_comments"

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	picture = models.ImageField(upload_to='profile_picture')

	def __str__(self):
		return 'Profile for: %s' % self.user.username