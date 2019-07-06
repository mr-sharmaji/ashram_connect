from django import forms
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        widget = {
            'title' :forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-text postcontent form-control'})
        }

class  CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widget = {
            'author' :forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-text form-control'})
        }




class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="<small>you@yourmailprovider.com</small>" ,widget=forms.TextInput(attrs={'class':'form-control form-text text-muted'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '<small class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<small><ul class="form-text text-muted"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<small class="form-text text-muted">Enter the same password as before, for verification.</small>'
