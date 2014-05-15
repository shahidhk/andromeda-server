from django import forms
from models import Kadai

class KadaiForm(forms.ModelForm):
    class Meta:
        model = Kadai
