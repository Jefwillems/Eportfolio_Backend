from django.views import generic


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['welcome'] = "Hello world"
        return context
