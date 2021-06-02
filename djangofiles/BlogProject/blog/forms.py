from django import forms
from .models import Comment, Answer

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            #'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
class AnonymousCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }

class AnswerForm(forms.Form):
    answer_content = forms.CharField(label='',max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'New Answer ..'}),required=False)
    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()
        return cleaned_data