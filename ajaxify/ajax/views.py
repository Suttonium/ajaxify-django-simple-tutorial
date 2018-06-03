from django.http import JsonResponse
from django.views.generic import FormView

from .forms import *


# Create your views here.

class JoinFormView(FormView):
    form_class = JoinForm
    template_name = 'ajax/ajax.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': "Successfully submitted data."
            }
            return JsonResponse(data)
        else:
            return response
