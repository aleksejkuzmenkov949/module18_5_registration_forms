from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password = forms.CharField(
        max_length=30,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        min_length=8  # минимальная длина пароля
    )
    repeat_password = forms.CharField(
        max_length=30,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
        min_length=8  # минимальная длина повтора пароля
    )
    age = forms.CharField(
        max_length=3,
        label="Введите свой возраст",
        widget=forms.TextInput(attrs={'placeholder': 'Введите свой возраст'})
    )


