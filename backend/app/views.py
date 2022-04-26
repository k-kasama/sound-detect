from django.views.generic.edit import FormView
from django.shortcuts import render, HttpResponse
from .forms import UploadFileForm

posted_data = {"text": "",
               "file": ""}

class IndexView(FormView):
    template_name = 'Index.html'
    form_class = UploadFileForm # forms.pyで作ったFormクラスをここで使う
    success_url = 'result' # formに入力された値が正しければこのURLに飛ぶ

    def form_valid(self, form):
        posted_data["text"] = form.data.get("text")
        posted_data["file"] = form.data.get("file")
        return super().form_valid(form)

def result_view(request):
    result = posted_data["text"]
    return render(request, 'result.html', {"name": result})