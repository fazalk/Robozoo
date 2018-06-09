from blog.models import Article
from forms import ArticleForm
from forms import EditForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

def home(request):
    article_list = Article.objects.all().order_by("-Date")
    paginator = Paginator(article_list, 5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request,'blog.html', {'articles': articles})

def articles(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    else:    
	    return render(request,'articles.html',
							 {'articles': Article.objects.all()})

def article(request, article_id=1):
	return render(request,'article.html',
							 {'article': Article.objects.get(id=article_id)})

def create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/blog')
    else:
        form = ArticleForm(initial={'Author': request.user.get_full_name()})
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request,'create_article.html', args)

@csrf_exempt
def edit(request, article_id=1):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
        
    article_no = Article.objects.get(id=article_id)  
    if request.POST:
        form = EditForm(request.POST, request.FILES, instance=article_no)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/blog/')
    else: 
        form = EditForm(instance=article_no)
    
    return render(request,'edit_article.html',
                             {'form': form, 'article': Article.objects.get(id=article_id)})


