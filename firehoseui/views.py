import xml.etree.ElementTree as ET

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

import forms
import models


### API for injecting results from a worker ###

@require_POST
def reports(request):
    for element in ET.iterparse(request):
        # do stuff to parse this element
        # save a models.Report
        pass
    # return list of file hashes we need uploaded
    return HttpResponse()


@require_POST
def upload_file(request):
    # completely untested. I'm assuming that the form's own parsing will do
    # the right things with the attached file.
    form = forms.SourceFileForm(request.POST)
    try:
        form.save()
    except ValueError:
        return HttpResponseBadRequest()

    return HttpResponse()
