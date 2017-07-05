from django.views import generic


class HomeView(generic.RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return '/api'
