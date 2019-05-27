from django import forms
from .models import Document
from dataCRUD.models import PRG_STUDENT_SITE 
from dataCRUD.models import ADR_STUDENTS
from dataCRUD.models import STUDENT_INTERNSHIP

tables=[('PRG_STUDENT_SITE',PRG_STUDENT_SITE),
        ('ADR_STUDENTS',ADR_STUDENTS),
        ('STUDENT_INTERNSHIP',STUDENT_INTERNSHIP),
       ]

filetypes=[('csv','csv'),
          ('text','txt'),
            ]

separators=[('comma','comma'),
         ('space','space'),
         ]
class DocumentForm(forms.ModelForm):
    fileFormat      =forms.CharField(label='File format:',widget=forms.Select(choices=filetypes))
    selectedtable   =forms.CharField(label='Tables:',widget=forms.Select(choices=tables))
    separator       =forms.ChoiceField(label='Separator:',choices=separators, widget=forms.RadioSelect())
    
    class Meta:
        model = Document
        fields = ('fileFormat','selectedtable','document',)