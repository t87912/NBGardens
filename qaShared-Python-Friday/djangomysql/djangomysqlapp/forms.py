from django import forms

class YearForm(forms.Form):
    year= forms.DateField(label='Year', max_length=100)
	
class LoginForm(forms.Form):
	user_name= forms.CharField(label='Username', max_length=100)
	pass_word= forms.CharField(label='Password', max_length=100)
	
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
	
class SalesForm(forms.Form)
	employeeid= forms.IntegerField(min_value=0)
	
class CustomerForm(forms.Form)
	amount= forms.IntegerField(min_value=0)
	customer_id= forms.IntegerField(min_value=0)
	productid= forms.IntegerField(min_value=0)

class DateForm(forms.Form)
	datefrom=forms.DateField(['%Y/%m/%d'])
	dateto=forms.DateField(['%Y/%m/%d'])

class ratingForm(forms.Form)
	county = forms.BooleanField(required=False)
	age = forms.BooleanField(required=False)
	gender = forms.BooleanField(required=False)