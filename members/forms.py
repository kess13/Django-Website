from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task





class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Імʼя користувача',
        help_text='Важливо! Пароль не більше 150 символів. Можна використовувати лише літери, цифри та @/./+/-/_',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Будь ласка, введіть імʼя користувача.',
            'max_length': 'Імʼя користувача не повинно перевищувати 150 символів.',
        }
    )
    password1 = forms.CharField(
        label='Пароль',
        help_text='Ваш пароль повинен містити не менше 8 символів і не бути часто використовуваним або повністю числовим.',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Будь ласка, введіть пароль.',
            'min_length': 'Пароль повинен містити не менше 8 символів.',
        }
    )
    password2 = forms.CharField(
        label='Підтвердження пароля',
        help_text='Введіть той же пароль, що й раніше, для перевірки.',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Будь ласка, підтверджте пароль.',
            'password_mismatch': 'Паролі не співпадають.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




class RegisterUserForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30, label='Імʼя')
    last_name = forms.CharField(max_length=30, label='Прізвище')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


from django import forms
from .models import Task

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    GRUZ_CHOICES = [
        ('corn', 'Кукурудза'),
        ('wheat', 'Пшениця'),
    ]

    gruz = forms.ChoiceField(
        choices=GRUZ_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Який груз',
        }),
        error_messages={
            'required': 'Будь ласка, виберіть тип груза.',
        }
    )

    massa = forms.DecimalField(
        label='Масса в кг',
        max_digits=20,
        decimal_places=4,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Масса в кг',
            'type': 'number',
            'step': '0.01',
            'min': '0',
        }),
        error_messages={
            'required': 'Будь ласка, введіть масу в кг.',
            'invalid': 'Будь ласка, введіть дійсне число.',
        }
    )

    litres = forms.DecimalField(
        label='Скільки літрів пального витратили',
        max_digits=20,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Скільки літрів пального витратили',
            'type': 'number',
            'step': '0.01',
            'min': '0',
        }),
        error_messages={
            'required': 'Будь ласка, введіть кількість літрів пального.',
            'invalid': 'Будь ласка, введіть дійсне число.',
        }
    )

    price = forms.DecimalField(
        label='Ціна за літр',
        max_digits=20,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ціна за літр',
            'type': 'number',
            'step': '0.01',
            'min': '0',
        }),
        error_messages={
            'required': 'Будь ласка, введіть ціну за літр.',
            'invalid': 'Будь ласка, введіть дійсне число.',
        }
    )

    misto = forms.CharField(
        label='Місто заправки',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Місто заправки',
        }),
        error_messages={
            'required': 'Будь ласка, введіть місто заправки.',
        }
    )

    punkt = forms.CharField(
        label='Мiсце завантаження',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пункт завантаження',
        }),
        error_messages={
            'required': 'Будь ласка, введіть пункт завантаження.',
        }
    )

    derzh_nomer = forms.CharField(
        label='Держномер авто',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Держномер авто',
        }),
        error_messages={
            'required': 'Будь ласка, введіть держномер авто.',
        }
    )

    ttn_nomer = forms.CharField(
        label='Номер ТТН',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер ТТН',
        }),
        error_messages={
            'required': 'Будь ласка, введіть номер ТТН.',
        }
    )

    skilki_vantazhu = forms.CharField(
        label='Кількість перевезеного вантажу',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Кількість перевезеного вантажу',
        }),
        error_messages={
            'required': 'Будь ласка, введіть кількість перевезеного вантажу.',
        }
    )

    odometr_viyizd = forms.CharField(
        label='Покази одометра при виїзді',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Покази одометра при виїзді',
        }),
        error_messages={
            'required': 'Будь ласка, введіть покази одометра при виїзді.',
        }
    )

    odometr_zayizd = forms.CharField(
        label='Покази одометра при заїзді',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Покази одометра при заїзді',
        }),
        error_messages={
            'required': 'Будь ласка, введіть покази одометра при заїзді.',
        }
    )

    zapravka_datetime = forms.DateTimeField(
        label='Заправка дата час',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Заправка дата час',
            'type': 'datetime-local',
        }),
        error_messages={
            'required': 'Будь ласка, введіть дату та час заправки.',
            'invalid': 'Будь ласка, введіть дійсну дату та час.',
        }
    )

    zavantazhennya_datetime = forms.DateTimeField(
        label='Дата і час завантаження',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата і час завантаження',
            'type': 'datetime-local',
        }),
        required=False,
    )


    rozvantazhennya_datetime = forms.DateTimeField(
        label='Дата і час розвантаження',
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата і час розвантаження',
            'type': 'datetime-local',
        }),
        required=False,
    )

    rozvantazhennya_mistse = forms.CharField(
        label='Місце розвантаження',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Місце розвантаження',
        }),
        required=False,
    )

    prymitky = forms.CharField(
        label='Примітки',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Примітки',
            'rows': 3,
        }),
        required=False,
    )

    class Meta:
        model = Task
        fields = [
            'misto', 'gruz', 'litres', 'price', 'massa', 'punkt', 'derzh_nomer',
            'ttn_nomer', 'skilki_vantazhu', 'odometr_viyizd', 'odometr_zayizd',
            'zavantazhennya_datetime',
            'rozvantazhennya_datetime', 'rozvantazhennya_mistse',
            'zapravka_datetime', 'prymitky'
        ]
