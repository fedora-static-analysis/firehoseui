from django.db import models

class SourceFile(models.Model):
    file = models.FileField(upload_to='source')
    # for SHA1 hash
    hash = models.CharField(max_length=42, db_index=True)


class Report(models.Model):
    """
    Exact schema to be determined after considering how the data will need to
    be accessed.
    """
    # this relationship may not be defined if we don't already have the source
    # file, and thus can be updated later once the file is uploaded.
    source = models.ForeignKey(SourceFile, related_name='reports', null=True)
    
