from django.shortcuts import render
from post.models import *
from django.shortcuts import render, redirect, get_object_or_404

def base_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'callsign/base_detail.html', {'post':post})