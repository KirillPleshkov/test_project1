from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            'title': 'Страница для теста меню',
        }
        return context
