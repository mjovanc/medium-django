from django.views.generic.base import TemplateView
from .models import BlogPost


class AboutView(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['blogposts'] = BlogPost.objects.all()
        return context
