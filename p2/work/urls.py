from django.conf.urls import url
from work import views

app_name = 'work'

urlpatterns=[
          url('page2/',views.GD,name='page2'),
          url('page3/',views.register,name='page3'),
          url('user_login/',views.user_login,name='user_login'),
]
