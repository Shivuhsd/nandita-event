from django import forms
from .models import Bookings, Feedback, Enquiry, Package


# Booking Form Generation
class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'package': forms.Select(attrs={'placeholder': '', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'placeholder': '', 'class': 'form-control', 'type':'date'}),
        }

# Feedback Form Generation
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'message': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }



# Enquiry Form Generation
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('__all__')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'message': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


# Package Form Generation
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ('__all__')


        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }