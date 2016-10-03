from django import forms

class YearForm(forms.Form):
    chosen_year= forms.CharField(label='Year', max_length=100)