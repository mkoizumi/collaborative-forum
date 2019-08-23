from django.views.generic import TemplateView

# renders to given url
class HomePage(TemplateView):
    template_name = 'index.html'  # homepage html

class LogoutPage(TemplateView):
    template_name = 'complete.html'
