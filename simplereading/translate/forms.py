from django import forms
from .models import Simple, Original, Vote, Simplify, Comment
from django.utils.safestring import mark_safe

class OriginForm(forms.ModelForm):
    hard_text = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')
    class Meta:
        model = Original
        fields = ('hard_text',)

class TestForm(forms.Form):
     original_text = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')

class SimpForm(forms.ModelForm):
    simple_text = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')
    class Meta:
        model = Simple
        exclude = ('hard',)

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label=mark_safe('Leave a comment<br />'))
    class Meta:
        model = Comment
        exclude = ('history',)

class SimplifyForm(forms.ModelForm):
    input = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')
    output = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='')
    class Meta:
        model = Simplify
        fields = ('input','output',)

class VoteForm(forms.ModelForm):
    votes = forms.IntegerField()
    class Meta:
        model = Vote
        fields = ('votes',)