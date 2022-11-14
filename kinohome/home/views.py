from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from .models import *
from users.models import *

# Create your views here.

class Home(ListView):
    model = PopularKino
    template_name = 'home/index.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kino Home'
        return context



class CategoryYear:

    def get_category(self):
        return Category.objects.all()

    def get_year(self):
        return Production_year.objects.all()



class Category_kino(CategoryYear, ListView):
    model = Kino
    template_name = 'home/category.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context



class Filter_kino(CategoryYear, ListView):
    template_name = 'home/category.html'
    context_object_name = 'posts'
    def get_queryset(self):
        if 'category' in self.request.GET and 'year' in self.request.GET:
            queryset = Kino.objects.filter(
                Q(production_year__in=self.request.GET.getlist("year")), Q(category__in=self.request.GET.getlist("category"))
            )
        else:
            queryset = Kino.objects.filter(
                Q(production_year__in=self.request.GET.getlist("year")) | Q(category__in=self.request.GET.getlist("category"))
            )
        return queryset



class PostByCategory(CategoryYear, ListView):
    template_name = 'home/category.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Kino.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context



class PostByProduction_year(CategoryYear, ListView):
    template_name = 'home/category.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = False


    def get_queryset(self):
        return Kino.objects.filter(production_year__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Production_year.objects.get(slug=self.kwargs['slug'])
        return context



class PostByCountry(CategoryYear, ListView):
    template_name = 'home/category.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = False


    def get_queryset(self):
        return Kino.objects.filter(сountry__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Country.objects.get(slug=self.kwargs['slug'])
        return context



class GetKino(FormMixin, DetailView,):
    model = Kino
    template_name = 'home/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Kino.objects.get(slug=self.kwargs['slug'])
        if str(self.request.user) != "AnonymousUser":
            r = [str(Favorites.objects.filter(user_f=self.request.user, kino_id=self.kwargs['pk']))]
            r1 = ["<QuerySet []>"]
            if r == r1:
                context['favorite_1'] = True
            else:
                context['favorite_1'] = False

            r = [str(Plans.objects.filter(user_f=self.request.user, kino_id=self.kwargs['pk']))]
            r1 = ["<QuerySet []>"]
            if r == r1:
                context['plan_1'] = True
            else:
                context['plan_1'] = False
        else:
            context['favorite_1'] = False
        return context

    def get_success_url(self):
        return reverse('category')



class Favorite_kino(ListView):
    template_name = 'home/favoriteORplans.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = True


    def get_queryset(self):

        return Favorites.objects.filter(user_f=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Любимые'
        return context



class Plans_kino(ListView):
    template_name = 'home/favoriteORplans.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = True


    def get_queryset(self):

        return Plans.objects.filter(user_f=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'В планах'
        return context



class Recommendations(ListView):
    template_name = 'home/recommendation.html'
    context_object_name = 'posts'
    paginate_by = 9
    allow_empty = True

    def get_queryset(self):
        return RecommendationsKino.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рекомендации'
        return context



def add_emailSub(request):
    return_dict = dict()
    data = request.POST
    email = data.get('email')
    new_email = EmailSub.objects.create(email=email)
    return JsonResponse(return_dict)



def add_favorite(request):
    return_dict = dict()
    user_f = request.user
    data = request.POST
    kino_id = data.get("kino_id")
    delete = data.get("kino_delete")
    plan = data.get("kino_plan")
    if plan == "True":
        if delete == "True":
            del_plan = Plans.objects.filter(user_f=user_f, kino_id=kino_id).delete()
        else:
            if "<QuerySet []>" == str(Plans.objects.filter(user_f=user_f, kino_id=kino_id)):
                new_plan = Plans.objects.create(user_f=user_f, kino_id=kino_id)
    else:
        if delete == "True":
            del_favorite = Favorites.objects.filter(user_f=user_f, kino_id=kino_id).delete()
        else:
            if "<QuerySet []>" == str(Favorites.objects.filter(user_f=user_f, kino_id=kino_id)):
                new_favorite = Favorites.objects.create(user_f=user_f, kino_id=kino_id)
    return JsonResponse(return_dict)



class Search(CategoryYear, ListView):
    template_name = 'home/search.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Kino.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context




class Get_Producer(ListView):
    template_name = 'home/authors.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Kino.objects.filter(producer__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Producer.objects.get(slug=self.kwargs['slug'])
        return context



class Get_Scenario(ListView):
    template_name = 'home/authors.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Kino.objects.filter(scenario__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Scenario.objects.get(slug=self.kwargs['slug'])
        return context



class Get_Author(ListView):
    template_name = 'home/authors.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Kino.objects.filter(author__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.objects.get(slug=self.kwargs['slug'])
        return context



