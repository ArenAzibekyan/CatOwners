from django import forms


class CatForm(forms.Form):
    name = forms.CharField(max_length=200,
                           label='Введите имя:',
                           error_messages={'required': 'Имя котика обязательно для заполнения',
                                           'invalid': 'Имя должно быть не длиннее 200 символов'})
    birthday = forms.DateField(input_formats=['%d/%m/%Y'],
                               label='Выберите дату рождения:',
                               error_messages={'required': 'Дата рождения обязательна для заполнения',
                                               'invalid': 'Дата рождения должна быть в формате ДД/ММ/ГГГГ'})
    breed = forms.CharField(max_length=200,
                            label='Введите породу:',
                            error_messages={'required': 'Порода котика обязательна для заполнения',
                                            'invalid': 'Порода должна быть не длиннее 200 символов'})
    hairiness = forms.CharField(max_length=200,
                                label='Опишите волосатость:',
                                error_messages={'required': 'Волосатость котика обязательна для заполнения',
                                                'invalid': 'Волосатость должна быть не длиннее 200 символов'})