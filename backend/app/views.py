from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "Index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Template View test index  "
        return context