from django import forms
from .models import Simple, Original, History

class SimplifyForm(forms.ModelForm):
    class Meta:
        model = Original
        fields = ('hard_text',)

class TestForm(forms.Form):
     original_text = forms.CharField(widget=forms.Textarea)