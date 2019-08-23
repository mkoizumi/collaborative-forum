from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta:
        # password2 for confirmation
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()


    # instead of setting label in html, let Form class generate it in here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'email'
        
