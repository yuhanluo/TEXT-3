from django import forms
from .models import Simple, Original, History

class SimplifyForm(forms.ModelForm):
    class Meta:
        model = Original
        fields = ('hard_text',)

class TestForm(forms.Form):
     original_text = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')
#simplified_text = forms.CharField(widget=forms.Textarea)