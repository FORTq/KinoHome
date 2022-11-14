from django import template
from home.models import Category, TrendKino, Sidebar

register = template.Library()


@register.inclusion_tag('home/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}


@register.inclusion_tag('home/menu_tpl_trend.html')
def show_menu_trend(menu_class='menu'):
    trends = TrendKino.objects.all()
    return {'trends1': trends, 'menu_class': menu_class}


@register.inclusion_tag('home/sidebar_tpl.html')
def snow_sidebar(menu_class='menu'):
    sidebar = Sidebar.objects.all()
    return {'sidebar': sidebar, 'menu_class': menu_class}