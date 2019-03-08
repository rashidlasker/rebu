from django import forms
from rebu.models import user, meal, cook, eater, plate, eater_rating, review, authenticator

class authenticatorForm(forms.ModelForm):
	user_id = forms.CharField(label='User_ID')
	authenticator = forms.CharField(label='Authenticator')
	date_created = forms.DateTimeField(label='Date_Created')

	class Meta:
		model = authenticator
		fields = ['user_id', 'authenticator', 'date_created']

class userForm(forms.ModelForm):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	street = forms.CharField(label='Street')
	zip_code = forms.CharField(label='Zip Code')
	state = forms.CharField(label='State')
	country = forms.CharField(label='Country')
	bio = forms.CharField(label='Bio')
	links = forms.CharField(label='Links')
	language = forms.CharField(label='Language')
	gender = forms.CharField(label='Gender')
	password = forms.CharField(label='Password', min_length=8)
	username = forms.CharField(label='Username')

	class Meta:
		model = user
		fields = ['first_name', 'last_name', 'street','zip_code','state','country','bio','links','language','gender', 'password', 'username']

class cookForm(forms.ModelForm):
	signature_dish = forms.CharField(label="Signature Dish")
	user = forms.ModelChoiceField(label="userid", queryset=user.objects.all())
	class Meta:
		model = cook
		fields = ['signature_dish', 'user']

class eaterForm(forms.ModelForm):
	user = forms.ModelChoiceField(label="userid", queryset=user.objects.all())
	class Meta:
		model = eater
		fields = ['user']

class mealForm(forms.ModelForm):
	calories = forms.CharField(label='Calories')
	description = forms.CharField(label='Description')
	spice = forms.CharField(label='Spice')
	price = forms.CharField(label='Price')
	tags = forms.CharField(label='Tags', max_length=150)
	takeout_available = forms.CharField(label='Takeout Available')
	num_plates = forms.CharField(label='Number of Plates', max_length=3)
	start = forms.CharField(label='Start Time/Date', max_length=50)
	end = forms.CharField(label='End Time/Date', max_length=50)
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	class Meta:
		model = meal
		fields = ['calories','description','spice','price','tags','takeout_available','num_plates','start','end','cook']

class plateForm(forms.ModelForm):
	meal = forms.ModelChoiceField(label='mealid', queryset=meal.objects.all())
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	class Meta:
		model = plate
		fields = ['meal','eater']

class eaterRatingForm(forms.ModelForm):
	rating = forms.IntegerField(label='Rating')
	description = forms.CharField(label='Description', max_length=150)
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	class Meta:
		model = eater_rating
		fields = ['rating','description','cook','eater']

class reviewForm(forms.ModelForm):
	rating = forms.IntegerField(label='Rating')
	description = forms.CharField(label='Description', max_length=150)
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	meal = forms.ModelChoiceField(label='mealid', queryset=meal.objects.all())
	class Meta:
		model = eater_rating
		fields = ['rating','description','eater','cook','meal']