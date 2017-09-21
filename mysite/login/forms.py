from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    c_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User

