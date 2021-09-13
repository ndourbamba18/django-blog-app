from django import forms  
from .models import Contact, Post

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )



class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')