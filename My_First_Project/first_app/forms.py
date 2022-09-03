from django import forms


class user_form(forms.Form):

    # <label for = "user_name" > Full Name: < /label >
    # <input type = "text" name = "user_name" placeholder="Enter your full name"  value = "" style="width:300px" required >
    # set style:
    user_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholdder': 'Enter your full name',
            'style': 'width: 300px'
        }))

    user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(
        attrs={
            'type': 'date'
        }
    ))

    # <label for = "user_email" > User Email: < /label >
    #  <input type = "email" name = "user_email" value = "" required >
    user_email = forms.EmailField(label="User Email")
