from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives


from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone

from urllib import quote_plus

from .forms import PostForm,contactform
from .models import Post

# Create your views here.

def homepage(request):
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
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
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
			"page_request_var":page_request_var,
			"today":today,
			"User":"reck",
		}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request,"home.html",context)

def aboutpage(request):
	context = {
		"title":"blog"
	}
	return render(request,"about.html",context)

def postpage(request,user_id = 19):
	instance = get_object_or_404(Post,user_id=user_id)
	#share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance":instance,
		#"share_string":share_string,
	}
	return render(request,"post.html",context)


def contactpage(request):
	form = contactform(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		uname =  form.cleaned_data.get("name")
		email =  form.cleaned_data.get("emailid")
		contact= form.cleaned_data.get("contact_no")
		msg = form.cleaned_data.get("message")
		print uname+email+contact+msg
		#Still validation is required jquery would help for client side validation
		subject = "Bloggo Message"
		message = uname+email+contact+msg
		from_email = "rakesh.gunduka@gmail.com"
		#from_email = EMAIL_HOST_USER
		to_list = ["rakesh.gunduka@gmail.com"]
		try:
			send_mail(subject,message,from_email,to_list,fail_silently=True)
		except Exception as e:
			print e
		instance.save()
		messages.success(request,"Successfully Created",extra_tags='success')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print "asdasd"
	context = {
		"form":form,
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
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
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
		#print form.cleaned_data.get("title")
		#instance.user = request.user
		instance.save()
		#message success
		#messages.success(request,"Successfully Created",extra_tags='success')
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request,"Not Successfully Created",extra_tags='error')

	# if request.method == "POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	# 	#Post.objects.create(title=title,content=content)
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,user_id):
	instance = get_object_or_404(Post,user_id=user_id)
	# if instance.draft or instance.publish > timezone.now().date():
	# 	if not request.user.is_staff or not request.user.is_superuser:
	# 		raise Http404
	# #instance = Post.objects.get(user_id=1)
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

def post_update(request,user_id):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post,user_id=user_id)
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

def post_delete(request,user_id=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post,user_id=user_id)
	instance.delete()
	messages.success(request,"Successfully deleted")
	return redirect("postss:home")
	
def suc(request):
	if request.POST:
		queryDict = request.POST
		myDict = dict(queryDict.iterlists())
		print myDict
	return HttpResponse("<h1>Success</h1>")
