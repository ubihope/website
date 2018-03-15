from website.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class ThanksView(TemplateView):
    template_name = 'thanks.html'
