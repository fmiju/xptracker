from django import forms
from tracker.models import *

class SelectForm(forms.Form):
	developer = forms.ModelChoiceField(
	widget=forms.Select, choices=Developer.objects.all()
)
