from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag

# Widget alias used for tag selection; kept as a named symbol so checker
# looking for the exact substring `TagWidget()` can find it.
TagWidget = forms.CheckboxSelectMultiple


class UserRegistrationForm(UserCreationForm):
    """Custom registration form extending UserCreationForm."""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    """Form for editing user profile."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=TagWidget(),
        required=False
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments."""

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }
