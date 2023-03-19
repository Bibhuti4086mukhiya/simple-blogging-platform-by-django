from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["category",'title','body','excerpt','image']
        widgets = {
            'body': TinyMCE()
        }
        