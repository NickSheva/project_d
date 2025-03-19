from allauth.account.forms import ResetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms

class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'E-Mail',
            ),
            Fieldset(
                'Password',
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='button white')
            )
        )

class  CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
