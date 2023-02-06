from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import Comment


class CommentForm(ModelForm):

  class Meta:
    model = Comment
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        submit = Submit('submit', 'Submit')
        self.helper.add_input(submit)
