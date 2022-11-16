from time import time
from post.models import *
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
#북마크
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def postlist(request):
    posts = Post.objects.filter(completed=False).order_by('end_date') # 모집 마감일 급한 것 부터 정렬
    enddate_list = []
    
    # 마감일이 이미 중복으로 존재하면 flag를 True로 변화시켜 출력되지 않게끔 만듦
    for p in posts:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True
      
    return render(request, 'post/postlist.html', {'posts':posts })

def post_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    random = Like.objects.filter(post=post)
    randomB = Dislike.objects.filter(post=post)
    context = {
           'posts':Post.objects.filter(id=id),
           'random' : random,
           'randomB' : randomB,
        }
   
    if (post.completed is True) :
        return render(request, 'post/result.html', context)
    else :
        return render(request, 'post/post_detail.html', context)

# def split_list(a_list):
#     half = len(a_list)//2
#     return a_list[:half], a_list[half:]

# A = ['a','b','c','d','e','f']
# B, C = split_list(A)
# print(B)
# print(C)


# 권한부여 

def post_completed(request, id):
    completed_post = Post.objects.get(id = id)
    completed_exercise = Exercise.objects.all()
    completed_sex = Sex.objects.all() 
    completed_post.completed=True
    completed_post.save()
    return redirect('post:completed_detail', completed_post.id)

def completed_postlist(request):
    posts = Post.objects.filter(completed=True).order_by('end_date') # 모집 마감일 급한 것 부터 정렬
    enddate_list = []
    
    # 마감일이 이미 중복으로 존재하면 flag를 True로 변화시켜 출력되지 않게끔 만듦
    for p in posts:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True
      
    return render(request, 'post/postlist.html', {'posts':posts })

def completed_detail(request, id) :
    post = get_object_or_404(Post, pk = id)
    random = Like.objects.filter(post=post)
    randomB = Dislike.objects.filter(post=post)
    context = {
           'posts':Post.objects.filter(id=id),
           'random' : random,
           'randomB' : randomB,
        }
   
    if (post.completed is True) :
        return render(request, 'post/result.html', context)
    else :
        return render(request, 'post/post_detail.html', context)
    return render(request, 'post/result.html', {'post':post})




def post_new(request):
    exercise = Exercise.objects.all()
    sex = Sex.objects.all()
    return render(request, 'post/post_new.html', {'exercise': exercise, "sex":sex})

def post_create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.url = request.POST['url']
    new_post.exercise = get_object_or_404(Exercise, id=request.POST['exercise'])
    new_post.count = request.POST['count']
    new_post.countB = request.POST['countB']
    new_post.sex = get_object_or_404(Sex, id=request.POST['sex'])
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    
    # 모집 마감일 추가
    new_post.end_date = request.POST['end_date']
    
    # 모집 시작시간, 마감시간 추가
    new_post.start_time = request.POST['start_time']
    new_post.end_time = request.POST['end_time']    
    
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('post:post_detail', new_post.id)


def post_edit(request, id):
    edit_post = Post.objects.get(id = id)
    sex = Sex.objects.all()
    exercise = Exercise.objects.all()
    return render(request, 'post/post_edit.html', {'post': edit_post,  'sex':sex, 'exercise': exercise})


def post_update(request, id):
    update_post = Post.objects.get(id=id)
    
    update_post.title = request.POST['title']
    update_post.url = request.POST['url']
    
    
    # try :
    #     update_post.sex = get_object_or_404(Sex, id = request.POST['sex'])
    # except: 
    #     update_post.sex = None
        
    # try :
    #     update_post.exercise = get_object_or_404(Exercise, id = request.POST['exercise'])
    # except: 
    #     update_post.exercise= None
    update_post.sex = get_object_or_404(Sex, id=request.POST['sex'])
    update_post.exercise = get_object_or_404(Exercise, id=request.POST['exercise'])
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.end_date = request.POST['end_date']
    
    # 모집 시작시간, 마감시간 추가
    update_post.start_time = request.POST['start_time']
    update_post.end_time = request.POST['end_time']  
    
    update_post.body = request.POST['body']
    update_post.save()
    
    return redirect('post:post_detail', update_post.id)

def post_delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect("post:postlist")
    
    
def soccer_list(request):
    soccer_list = []
    s = Exercise.objects.filter(name="축구")
    soccer_post = Post.objects.filter(exercise__in=s, completed=False).order_by('end_date')
    
    for post in soccer_post:
        soccer_list.append(post)
        
    enddate_list = []    
    for p in soccer_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/soccer_list.html', {'soccer_list': soccer_list})

def basketball_list(request):
    basketball_list = []
    bsk = Exercise.objects.filter(name="농구")
    bsk_post = Post.objects.filter(exercise__in=bsk, completed=False).order_by('end_date')
    
    for post in bsk_post:
        basketball_list.append(post)
        
    enddate_list = []    
    for p in bsk_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/basketball_list.html', {'basketball_list': basketball_list})

def volleyball_list(request):
    volleyball_list = []
    v = Exercise.objects.filter(name="족구")
    v_post = Post.objects.filter(exercise__in=v, completed=False).order_by('end_date')
    
    for post in v_post:
        volleyball_list.append(post)
    enddate_list = []    
    for p in v_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/volleyball_list.html', {'volleyball_list': volleyball_list})

def baseball_list(request):
    baseball_list = []
    b = Exercise.objects.filter(name="야구")
    b_post = Post.objects.filter(exercise__in=b, completed=False).order_by('end_date')
    
    for post in b_post:
        baseball_list.append(post)
    enddate_list = []    
    for p in b_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/baseball_list.html', {'baseball_list': baseball_list})


def tennis_list(request):
    tennis_list = []
    t = Exercise.objects.filter(name="테니스")
    t_post = Post.objects.filter(exercise__in=t, completed=False).order_by('end_date')
    
    for post in t_post:
        tennis_list.append(post)
    enddate_list = []    
    for p in t_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/tennis_list.html', {'tennis_list': tennis_list})

def badminton_list(request):
    badminton_list = []
    b = Exercise.objects.filter(name="배드민턴")
    b_post = Post.objects.filter(exercise__in=b, completed=False).order_by('end_date')
    
    for post in b_post:
        badminton_list.append(post)
    enddate_list = []    
    for p in b_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/badminton_list.html', {'badminton_list': badminton_list})

def running_list(request):
    running_list = []
    r = Exercise.objects.filter(name="산책/러닝")
    r_post = Post.objects.filter(exercise__in=r, completed=False).order_by('end_date')
    
    for post in r_post:
        running_list.append(post)
    enddate_list = []    
    for p in r_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/running_list.html', {'running_list': running_list})

def etc_list(request):
    etc_list = []
    e = Exercise.objects.filter(name="기타")
    e_post = Post.objects.filter(exercise__in=e, completed=False).order_by('end_date')
    
    for post in e_post:
        etc_list.append(post)
    enddate_list = []    
    for p in e_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/etc_list.html', {'etc_list': etc_list})


# 완료된

def completed_soccer_list(request):
    soccer_list = []
    s = Exercise.objects.filter(name="축구")
    soccer_post = Post.objects.filter(exercise__in=s, completed=True).order_by('end_date')
    
    for post in soccer_post:
        soccer_list.append(post)
        
    enddate_list = []    
    for p in soccer_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/soccer_list.html', {'soccer_list': soccer_list})

def completed_basketball_list(request):
    basketball_list = []
    bsk = Exercise.objects.filter(name="농구")
    bsk_post = Post.objects.filter(exercise__in=bsk, completed=True).order_by('end_date')
    
    for post in bsk_post:
        basketball_list.append(post)
        
    enddate_list = []    
    for p in bsk_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/basketball_list.html', {'basketball_list': basketball_list})

def completed_volleyball_list(request):
    volleyball_list = []
    v = Exercise.objects.filter(name="족구")
    v_post = Post.objects.filter(exercise__in=v, completed=True).order_by('end_date')
    
    for post in v_post:
        volleyball_list.append(post)
    enddate_list = []    
    for p in v_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/volleyball_list.html', {'volleyball_list': volleyball_list})

def completed_baseball_list(request):
    baseball_list = []
    b = Exercise.objects.filter(name="야구")
    b_post = Post.objects.filter(exercise__in=b, completed=True).order_by('end_date')
    
    for post in b_post:
        baseball_list.append(post)
    enddate_list = []    
    for p in b_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/baseball_list.html', {'baseball_list': baseball_list})


def completed_tennis_list(request):
    tennis_list = []
    t = Exercise.objects.filter(name="테니스")
    t_post = Post.objects.filter(exercise__in=t, completed=True).order_by('end_date')
    
    for post in t_post:
        tennis_list.append(post)
    enddate_list = []    
    for p in t_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/tennis_list.html', {'tennis_list': tennis_list})

def completed_badminton_list(request):
    badminton_list = []
    b = Exercise.objects.filter(name="배드민턴")
    b_post = Post.objects.filter(exercise__in=b, completed=True).order_by('end_date')
    
    for post in b_post:
        badminton_list.append(post)
    enddate_list = []    
    for p in b_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/badminton_list.html', {'badminton_list': badminton_list})

def completed_running_list(request):
    running_list = []
    r = Exercise.objects.filter(name="산책/러닝")
    r_post = Post.objects.filter(exercise__in=r, completed=True).order_by('end_date')
    
    for post in r_post:
        running_list.append(post)
    enddate_list = []    
    for p in r_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/running_list.html', {'running_list': running_list})

def completed_etc_list(request):
    etc_list = []
    e = Exercise.objects.filter(name="기타")
    e_post = Post.objects.filter(exercise__in=e, completed=True).order_by('end_date')
    
    for post in e_post:
        etc_list.append(post)
    enddate_list = []    
    for p in e_post:
        if p.end_date not in enddate_list:
            enddate_list.append(p.end_date)
        else:
            p.flag_enddate = True

    return render(request, 'post/etc_list.html', {'etc_list': etc_list})



    
# 신청하기
@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    
    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"

    context = {
        "like_count" : post.like_count,
        "result" : result,
    }

    return HttpResponse(json.dumps(context), content_type="apllication/json")

def my_like(request, user_id):
    user = User.objects.get(id=user_id)
    like_list = Like.objects.filter(user=user)
    context = {
        'like_list' : like_list,
    }
    return render(request, 'accounts/mypage.html', context)


@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")
