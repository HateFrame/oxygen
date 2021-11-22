from .models import RequestList
from django.forms import ModelForm, TextInput, Textarea


class RequestListForm(ModelForm):
    class Meta:
        model = RequestList
        fields = ('user', 'phone_number', 'email', 'comment')
        labels = {'user': 'Имя', 'phone_number': 'Номер телефона',
                  'email': 'Электронная почта', 'comment': 'Комментарий к заявке'}
        widgets = {
            'user': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail@mail.com'
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'id': 'commentField',
                'rows': '3'
            })
        }

