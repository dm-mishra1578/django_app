from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    #validation for the name field
    def clean_name(self):
        data = self.cleaned_data['name']
        if "spam" in data.lower():
            raise forms.ValidationError("No spam allowed!")
        return data
