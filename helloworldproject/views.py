from django.http import HttpResponse
from django.views.generic import TemplateView
# funvtion based viewで実装する
def helloworldfunction(request):
    #googleで'django httpresponse'などと検索して公式ドキュンメント等を参考に進めていく
    returnedobject =  HttpResponse('<h1>hello world<h1>')
    return returnedobject

# class based viewで実装する
#djangoが用意しているTemplateViewを継承する
class HelloWorldClass(TemplateView):
    #template_nameとはこのclassを呼び出した際に返すhtmlファイルの場所を指定する
    template_name = 'hello.html'