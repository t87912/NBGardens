from django.contrib.auth.models import User
from django import forms

class YearForm(forms.Form):
    year= forms.CharField(label='Year', max_length=100)
	
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
	
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
	
class SalesForm(forms.Form):
	employeeid= forms.IntegerField(min_value=0)
	
class CustomerForm(forms.Form):
	amountmin= forms.IntegerField(min_value=0)
	customer_id= forms.IntegerField(min_value=0)
	productid= forms.IntegerField(min_value=0)

class DateForm(forms.Form):
	datefrom=forms.DateField(['%Y/%m/%d'])
	dateto=forms.DateField(['%Y/%m/%d'])

class ratingForm(forms.Form):
	county = forms.BooleanField(required=False)
	age = forms.BooleanField(required=False)
	gender = forms.BooleanField(required=False)