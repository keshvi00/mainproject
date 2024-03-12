from django.core import validators
from django import forms
from .models import Admin
class tasksentry(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['Employee_ID','Task_Domain','Task_Title','Start_Date','End_Date']
        widgets={
                'Employee_ID':forms.NumberInput(attrs={'class':'form-control bg-white','placeholder':'Enter Your ID'}),
                'Task_Domain':forms.TextInput(attrs={'class':'form-control bg-white text-ml-2','placeholder':'Enter Task Domain'}),
                 'Task_Title':forms.TextInput(attrs={'class':'form-control bg-white text-ml-2','placeholder':'Enter Title of Task'}),
                'Start_Date': forms.DateInput(attrs={'class':'form-control bg-white w-25','placeholder':'Start Date of Task'}),
                
                'End_Date': forms.DateInput(attrs={'class':'form-control bg-white w-25','placeholder':'End Date of Task'}),
                }
        Start_Date=forms.DateTimeField(
            widget=forms.DateInput
            (attrs= {'class':'form-control bg-white w-25', 'type':'Date' }
            ),
            initial='2024-02-20'
        )
    