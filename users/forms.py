from django import forms
from django.contrib.auth import get_user_model, authenticate
from captcha.fields import ReCaptchaField, ReCaptchaV2Checkbox, ReCaptchaV3


user_model = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control mb-4',
        'id': 'defaultLoginFormEmail',
        'name': 'username',
        'aria-describedby': 'emailHelp',
        'placeholder': "E-mail",
        'maxlength': 100,
        'required': True
    }))

    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'class': 'form-control mb-4',
        'id': 'defaultLoginFormPassword',
        'name': 'password',
        'placeholder': 'Password',
        'maxlength': 100,
        'required': True
    }))

    captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox(attrs={
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        email_qs = user_model.objects.filter(email=self.cleaned_data.get('username'))

        if email_qs is None:
            raise forms.ValidationError('BLYABLYA ERRROR')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("ERROR!")
        if not username:
            raise forms.ValidationError('EEROR USERNAME')
        if not password:
            raise forms.ValidationError('EEROR PASSWORD')

        return super(LoginForm, self).clean()


class SignupForm(forms.ModelForm):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'input',
        'id': 'username',
        'name': 'username',
        'placeholder': "Enter your username",
        'maxlength': 100,
        'required': True
    }))

    email = forms.EmailField(label='', widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'input',
        'id': 'email',
        'name': 'email',
        'placeholder': 'Email',
        'maxlength': 100,
        'required': True
    }))

    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'class': 'input',
        'id': 'password',
        'name': 'password',
        'placeholder': 'Password',
        'maxlength': 100,
        'required': True
    }))

    password2 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'class': 'input',
        'id': 'password2',
        'name': 'password',
        'placeholder': 'Password',
        'maxlength': 100,
        'required': True
    }))

    captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox(attrs={


    }))


    class Meta:
        model = user_model
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        email_qs = user_model.objects.filter(email=email)
        
        if email_qs.exists():
            raise forms.ValidationError('Email is already used')
        
        if password != password2:
            raise forms.ValidationError('Passwords must match!')
        
        return super(SignupForm, self).clean()
