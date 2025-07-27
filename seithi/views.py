from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import News,Review, ReviewMag,Tag,Magazine,MagazineSubscriber



def news(request):
    news = News.objects.all()[:30] 
    tags = Tag.objects.all()
    context = {'news': news,'tags':tags}
    return render(request, 'seithi/news.html', context)

def new(request, pk):
    projectobj = get_object_or_404(News, id=pk)
    tags = projectobj.tags.all()
    latest_news = News.objects.exclude(id=pk).order_by('-published_date')[:3]
    matched_news = News.objects.filter(tags__in=tags).exclude(id=pk).distinct().order_by('-published_date')[:30]

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            Review.objects.create(news=projectobj, name=name, body=body)
            return redirect('single-news', pk=pk)

    comments = projectobj.review_set.all().order_by('-created')

    context = {
        'new': projectobj,
        'tags': tags,
        'latest_news': latest_news,
        'matched_news': matched_news,
        'comments': comments,
    }

    return render(request, 'seithi/single-news.html', context)

def new_news(request):
    news = News.objects.all().order_by('-published_date')
    tags = Tag.objects.all()
    context = {
        'news': news,
        'tags': tags,
    }
    return render(request, 'seithi/new_news.html', context)


def news_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    news = News.objects.filter(tags=tag).order_by('-published_date')  # No slicing here!
    tags = Tag.objects.all()  # For the dropdown
    return render(request, 'seithi/tag_news.html', {'news': news, 'tags': tags, 'tag_name': tag_name})

def magazine_page(request):
    magazines = Magazine.objects.order_by('-published_date')
    show_pdf = False
    selected_magazine = None

    if request.method == "POST":
        email = request.POST.get('email')
        mag_id = request.POST.get('magazine_id')

        if email and mag_id:
            MagazineSubscriber.objects.get_or_create(email=email)
            selected_magazine = Magazine.objects.get(id=mag_id)
            show_pdf = True

    return render(request, 'seithi/magazine_page.html', {
        'magazines': magazines,
        'show_pdf': show_pdf,
        'selected_magazine': selected_magazine,
    })
def single_magazine(request,pk):
    magazine = Magazine.objects.get(title = pk)
    show_pdf = True
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        if name and body:
            ReviewMag.objects.create(Magazine=magazine, name=name, body=body)
            return redirect('single-mag', pk=pk)

    comments = ReviewMag.objects.filter(Magazine=magazine).order_by('-created')
    return render(request, 'seithi/single-mag.html',{'magazine' : magazine,'show_pdf':show_pdf,'comments':comments})