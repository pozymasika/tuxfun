from django import forms

class PostAddition(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    category = 
