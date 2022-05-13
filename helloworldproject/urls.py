from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldClass

urlpatterns = [
    #ここで定義したpathによってadmin画面に遷移する
    #一致しているかどうかの判断は上から順に行われる(上の段階で一致すれば下は無視される)
    #path('helloworld/', admin.site.urls),
    #path('helloworld2/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloWorldClass.as_view()),
    path('app/', include('helloworldapp.urls'))
]
