from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'orderby_records'
	queryset = BlogPost.objects.order_by('-posted_at')
	paginate_by = 3
	
class BlogDetail(DetailView):
	template_name = 'post.html'
	model = BlogPost

class ScienceView(ListView):
	template_name = 'science_list.html'
	model = BlogPost
	context_object_name = 'science_records'
	queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
	paginate_by = 2

class DailylifeView(ListView):
	template_name = 'dailylife_list.html'
	model = BlogPost
	context_object_name = 'dailylife_records'
	queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
	paginate_by = 2

class MusicView(ListView):
	template_name = 'music_list.html'
	model = BlogPost
	context_object_name = 'music_records'
	queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
	paginate_by = 2


'''	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context
		'''
		
