from django import template
from post.models import Post

register = template.Library()


@register.inclusion_tag('all_post.html')
def get_all_post():
    all_post = Post.objects.all().filter(draft=True).order_by('postdate')
    return {'all_posts': all_post}
