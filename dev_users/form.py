from django.forms import forms, ModelForm
from  django.contrib.auth .forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['first_name','email','username','password1','password2']
        labels ={
            'first_name':'Name',
            'username':'UserName'
        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name ,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio','profile_image','social_twitter','social_github']
        labels ={
            'username':'UserName',
            'name': 'Name',
            'email':'Email',

        }

    def __init__(self,*args,**kwargs):
        super(ProfileEditForm,self).__init__(*args,**kwargs)

        for name , filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']


    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name ,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
