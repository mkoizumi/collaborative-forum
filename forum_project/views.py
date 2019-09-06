from django.views.generic import TemplateView

# renders to given url
class HomePage(TemplateView):
    template_name = 'index.html'  # homepage html

# simple completed message page
class LogoutPage(TemplateView):
    template_name = 'complete.html'
