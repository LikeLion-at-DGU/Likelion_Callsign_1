from django.urls import path
from .views import *
from . import views

app_name = 'post'
urlpatterns = [
    path('', postlist, name = "postlist"),
    path('<int:id>/', post_detail, name="post_detail"),
    path('post_new/', post_new, name = "post_new"),
    path('post_create/', post_create, name="post_create"),
    path('post_edit/<int:id>', post_edit, name="post_edit"),
    path('post_update/<int:id>', post_update, name="post_update"), 
    path('post_delete/<int:id>', post_delete, name="post_delete"),   
    
    
    path('soccer_list/', soccer_list, name="soccer_list"),  
    path('basketball_list/', basketball_list, name="basketball_list"), 
    path('baseball_list/', baseball_list, name="baseball_list"), 
    path('badminton_list/', badminton_list, name="badminton_list"), 
    path('volleyball_list/', volleyball_list, name="volleyball_list"), 
    path('tennis_list/', tennis_list, name="tennis_list"), 
    path('etc_list/', etc_list, name="etc_list"), 
    # 모집 완료 후 보이는거
    path('completed_detail/<int:id>', completed_detail, name="completed_detail"),
    path('completed_postlist', completed_postlist, name="completed_postlist"),
    path('completed_soccer_list/', completed_soccer_list, name="completed_soccer_list"),  
    path('completed_basketball_list/', completed_basketball_list, name="completed_basketball_list"), 
    path('completed_baseball_list/', completed_baseball_list, name="completed_baseball_list"), 
    path('completed_badminton_list/', completed_badminton_list, name="completed_badminton_list"), 
    path('completed_volleyball_list/',completed_volleyball_list, name="completed_volleyball_list"), 
    path('completed_tennis_list/', completed_tennis_list, name="completed_tennis_list"), 
    path('completed_running_list/',completed_running_list, name="completed_running_list"), 
    path('completed_etc_list/', completed_etc_list, name="completed_etc_list"), 
    # 모집완료
    path('<int:id>/post_completed/',post_completed, name="post_completed"),
    path('like_toggle/<int:post_id>', like_toggle, name="like_toggle"),
    path('my_like/<int:user_id>', my_like, name="my_like"),
    path('dislike_toggle/<int:post_id>/',dislike_toggle,name="dislike_toggle"),
    # 랜덤매칭
    # path('split_list', split_list, name="split_list"),

]
