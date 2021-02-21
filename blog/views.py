from django.views.generic import ListView, DetailView
from django.core import paginator
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from django.core.paginator import Paginator

# def Home(request, page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {'title': 'Home page', 'articles': articles}
#     return render(request, 'blog/home.html', context)


class ArticleList(ListView):
    # model = Article
    # template_name = 'blog/home.html'
    # context_object_name = 'articles'
    queryset = Article.objects.published()
    paginate_by = 4


# def Detail_article(request, slug):
#     context = {
#         'article': get_object_or_404(
#             Article.objects.published(),
#             slug=slug,
#         )
#     }
#     return render(request, 'blog/detail.html', context)


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(
            Article.objects.published(),
            slug=slug,
        )


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 3)
#     articles = paginator.get_page(page)

#     context = {'category': category, 'articles': articles}
#     return render(request, 'blog/category-page.html', context)


class DetailList(ListView):

    paginate_by = 2
    template_name = 'blog/category-page.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug, status=True)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context
    