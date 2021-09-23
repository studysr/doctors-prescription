from django import forms
from prescription.models import Patient, Medicine

# form used for supplier

FAVORITE_COLORS_CHOICES = (
('one', 'ONE'),
('two', 'TWO'),
('three', 'THREE'),)





class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'title' : 'Alphabets and Spaces only'})
        self.fields['age_y'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only'})
        self.fields['cc'].widget.attrs.update({'class': 'textinput form-control'})
    

    class Meta:
        model = Patient
        fields = ['name','others_test', 'age_y', 'age_m', 'age_d','sex','cc','oe','pulse','bp','test',]
        widgets = {
            'cc' : forms.Textarea(attrs = {'class' : 'textinput form-control','rows'  : '4'}),
            'test': forms.CheckboxSelectMultiple()
        }


class medForm(forms.ModelForm):
    model= Medicine()
    class Meta:
        model = Medicine
        fields = ['patientname',
            'test_result',
            'next_visit',
            'diagonosis',
            'advice',
            'med1',
            'rule1',
            'med2',
            'rule2',
            'med3',
            'rule3',
            'med4',
            'rule4',
            'med5',
            'rule5',
            'med6',
            'rule6',
            'med7',
            'rule7',
            'med8',
            'rule8',
            'med9',
            'rule9',
            'med10',
            'rule10'
        ]