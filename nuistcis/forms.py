from django import forms
from django.contrib.auth.models import User

from .models import Department, Activity, News , Newsimages, Note , Programs ,Programstype


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['goal', 'department_title', 'genre', 'department_logo']


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['activity_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class NewsCreateForm(forms.ModelForm):
    news_mainphoto = forms.ImageField(label='news_mainphoto')
    class Meta:
        model = News
        fields = ['news_title', 'news_content', 'news_date', 'new_author', 'news_mainphoto']


class ProgramsCreateForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = ['program_name', 'program_description', 'program_intake', 'program_duration', 'program_tuition', 'program_mainphoto']


class ProgramstypeCreateForm(forms.ModelForm):
    class Meta:
        model = Programstype
        fields = ['programs_type_name', 'programs_type_description']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_content', 'note_date', 'note_author']


class NewsDetailForm(forms.ModelForm):
    news_image = forms.ImageField(label='news_image')

    class Meta:
        model = Newsimages
        fields = ('news_image',)

