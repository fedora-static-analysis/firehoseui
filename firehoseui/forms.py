from django.forms import ModelForm

import models

class SourceFileForm(ModelForm):
    class Meta:
        model = models.SourceFile
