from django import forms
from .models import *
from datetime import date




class BookForm(forms.ModelForm):

   
    title = forms.CharField(label="First Name", required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))
    author = forms.CharField(label="Author", required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))
    
    
    book_code = forms.CharField(label="Book Code", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    no_of_book = forms.CharField(label="Joining Date", required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))   
    summary = forms.CharField(label="Author", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
   

    class Meta:
        model = Book
        fields = ['title', 'author', 'book_code', 'no_of_book', 'summary']

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        title = cleaned_data.get("title")
        author = cleaned_data.get("author")
        book_code = cleaned_data.get("book_code")
        no_of_book = cleaned_data.get("no_of_book")
        summary = cleaned_data.get("summary")
        
        return cleaned_data


