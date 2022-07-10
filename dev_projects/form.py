from django.forms import ModelForm,widgets
from .models import Project,Review
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','vote_total','vote_ratio','tags']

        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args ,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name ,filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class':'input'}
        # )
        #
        # self.fields['description'].widget.attrs.update({
        #     'class':'input'
        # })

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value':'Place Your Vote',
            'body':'Add a comment for this project'
        }

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})
