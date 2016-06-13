from urllib import quote_plus

from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect

from .forms import PostForm
from .models import Post
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
# Create your views here.

def homepage(request):
	context = {
		"title":"blog"
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request,"home.html",context)

def aboutpage(request):
	context = {
		"title":"blog"
	}
	return render(request,"about.html",context)

def postpage(request):
	context = {
		"title":"blog"
	}
	return render(request,"post.html",context)

def contactpage(request):
	context = {
		"title":"blog"
	}
	return render(request,"contact.html",context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	# if request.user.is_staff or request.user.is_superuser:
	queryset_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query) 
			).distinct()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
		print 
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
			"object_list" : queryset,
			"title":"Posts",
			"page_request_var":page_request_var,
			"today":today,
		}
	return render(request,"post_list.html",context)
	#return render(request,"index.html ",{'contact':['Heyy!!If you would like to contact me,please email me','rakesh.gunduka@gmail.com']})
	#return HttpResponse("<h1>Hello</h1>")


def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	# # if not request.user.is_authenticated():
	# 	raise Http404

	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		#instance.user = request.user
		instance.save()
		#message success
		messages.success(request,"Successfully Created",extra_tags='success')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Not Successfully Created",extra_tags='error')

	# if request.method == "POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	# 	#Post.objects.create(title=title,content=content)
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	#instance = Post.objects.get(id=1)
	#instance = get_object_or_404(Post,title="post123")
	
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance":instance,
		"share_string":share_string,
	}
	# # if request.user.is_authenticated():
	# 	context = {
	# 		"title":["Anything about title 1","another statement"]
	# 	}
	# else:
	# 	context = {
	# 		"title":["This is another","here is another"]
	# 	}
	return render(request,"post_detail.html",context)

	#return HttpResponse("<h1>Detail</h1>")

def post_update(request,id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,request.FILES or None,instance = instance )
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
		#message success
		messages.success(request,"Successfully  Updated",extra_tags='success')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully deleted")
	return redirect("postss:list")
	
