from django import forms

class YearForm(forms.Form):
    chosen_year= forms.CharField(label='Year', max_length=100)
	
class LoginForm(forms.Form):
    user_name= forms.CharField(label='Username', max_length=100)
	pass_word= forms.CharField(label='Password', max_length=100)