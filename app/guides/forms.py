from django import forms


class QNAForm(forms.Form):

    question = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label='Your Large Text Field'
    )
    answer = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label='Your Large Text Field'
    )
    search_terms=forms.CharField(label="Search tags seperated by commas")
    
        
class TagSearch(forms.Form):
    tag = forms.CharField(label='Search Tags')