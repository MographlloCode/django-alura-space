from django import forms

class LoginForms(forms.Form):
    ''' Form maker and manager for Login '''

    login_name = forms.CharField(
        label = 'Name',
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

class RegisterForms(forms.Form):
    name = forms.CharField(
        label = 'Name',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "i.e.: Gustavo Mello"
            }
        )
    )
    email = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "i.e.: youremail@goeshere.com"
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

    confirm_password = forms.CharField(
        label = 'Confirm Password',
        required = True,
        max_length = 60,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Type your password again"
        })
    ) 

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            name = name.strip()
            if " " in name:
                raise forms.ValidationError('Name can\'t have spaces')
            else:
                return name
            
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('confirm_password')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Passwords doesn\'t match')
            else:
                return password_confirm