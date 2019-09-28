from django import forms


class CommentForm(forms.Form):

    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True, label='E-Mail:')
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=True, label='Betreff:')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}), required=True, label= 'Nachricht:', max_length=900)
