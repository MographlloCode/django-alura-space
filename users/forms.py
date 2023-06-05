from django import forms

class LoginForms(forms.Form):
    ''' Form maker and manager for Login '''

    login_name = forms.CharField(
        label = 'Login Name',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "i.e.: Gustavo Mello"
            }
        )
    )

    password = forms.CharField(
        label = 'Password',
        required = True,
        max_length = 60,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Type your password"
        })
    ) 