from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bio'}))
    links = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Links'}))
    language = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Language'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gender'}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class MealForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    calories = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Calories'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}))
    spice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Spice'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}))
    tags = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tags'}))
    takeout_available = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class':'custom-control-input', 'id':'takeoutCheck'}))
    num_plates = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Num Plates'}))
    start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Start'}))
    end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'End'}))