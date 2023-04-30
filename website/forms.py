from django import forms
from .models import company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['cemail', 'cpassw', 'cname', 'ccity', 'cstate', 'czip', 'ccost', 'cdis', 'cimage']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)