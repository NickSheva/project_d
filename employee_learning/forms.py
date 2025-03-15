from allauth.account.forms import ResetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].help_text = ""  # Удаляем текст подсказки

        # Добавляем crispy-forms для улучшения макета
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "Reset Password",
                Field("email", css_class="form-control"),  # Поле email
            ),
            ButtonHolder(
                Submit(
                    "submit", "Reset Password", css_class="btn btn-primary"
                )  # Кнопка отправки
            ),
        )


# from allauth.account.forms import ResetPasswordForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
# from django import forms
# class MyForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Fieldset(
#                 'E-Mail',
#             ),
#             Fieldset(
#                 'Password',
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Save', css_class='button white')
#             )
#         )

# class  CustomResetPasswordForm(ResetPasswordForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].help_text = ''