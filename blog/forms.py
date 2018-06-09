from django import forms
from models import Article

class ArticleForm(forms.ModelForm):  

    Image = forms.FileField(required=False)
    Text = forms.CharField(widget=forms.Textarea(attrs={'selector': 'textarea'}))

    class Meta:
        model = Article
        fields = ('Title', 'Date', 'Author', 'Text', 'Image')

class EditForm(forms.ModelForm):  

    Image = forms.FileField(required=False)
    Text = forms.CharField(widget=forms.Textarea(attrs={'selector': 'textarea'}))

    class Meta:
        model = Article
        fields = ('Title', 'Date', 'Text', 'Image')

