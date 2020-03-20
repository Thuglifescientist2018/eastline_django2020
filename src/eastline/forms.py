from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {"username": None,}
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        db_username = User.objects.filter(username=username)
        if db_username.exists():
            raise forms.ValidationError("That username is already taken")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_in_db = User.objects.filter(email=email)
        if email_in_db.exists():
            raise forms.ValidationError("This email is already taken. Please use another email address")
        return email
    
    def save(self, commit=True):
        user = super (SignUpForm , self ).save(commit=False)
     

        if commit :
            user.is_staff = True
            user.save()

        return user
    

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


