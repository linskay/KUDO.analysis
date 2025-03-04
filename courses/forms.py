from django import forms
from .models import Course

class CoursesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CoursesForm, self).__init__(*args, **kwargs)

        self.fields['name_course'].widget.attrs.update({'class': 'form-control','placeholder': 'Введите название курса'})
        self.fields['description_course'].widget.attrs.update({'class': 'form-control','placeholder': 'Введите описание курса'})
        self.fields['photo_course'].widget.attrs.update({'class': 'form-control',})
        self.fields['pay_course'].widget.attrs.update({'class': 'form-control',})
        self.fields['students'].widget.attrs.update({'class': 'form-control',})



    class Meta:
        model = Course
        fields = ['name_course','description_course','photo_course','pay_course','students']




    def clean_photo_course(self):
        image = self.cleaned_data['photo_course']
        if type(image) is not bool and hasattr(image, 'size'):
            if image.size > 1024 * 1024:  # 1MB
                raise forms.ValidationError('Изображение не может быть больше 1MB.')
        return image


