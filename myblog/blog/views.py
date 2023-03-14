from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from .models import Publication
from .models import Like

from .form import CommentForm


# noinspection PyMethodMayBeStatic
class IndexPage(View):
    """Publications view"""

    def get(self, request):
        """

        :param request:
        :return:
        """
        publications = Publication.objects.all()

        return render(request, 'blog/blog.html', {'publication_list': publications})


# noinspection PyMethodMayBeStatic
class PublicationPage(View):
    """Publication view"""

    def get(self, request, pk):
        publication = Publication.objects.get(id=pk)
        return render(request, 'blog/publication.html', {'publication': publication})


# noinspection PyMethodMayBeStatic
class AddComment(View):
    """Leaving comments"""

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.publication_id = pk
            form.save()

        return redirect(f'/{pk}')


class AddLike(View):
    """Add like to publication"""

    # noinspection PyMethodMayBeStatic
    def get(self, request, pk):
        client_ip = get_client_ip(request)
        try:
            Like.objects.get(ip_address=client_ip, publication_id=pk)
        except Like.DoesNotExist:
            like = Like()
            like.ip_address = client_ip
            like.publication_id = pk
            like.save()

        return redirect(f'/{pk}')


class DelLike(View):
    """Like deletion"""

    # noinspection PyMethodMayBeStatic
    def get(self, request, pk):
        client_ip = get_client_ip(request)
        try:
            like = Like.objects.get(ip_address=client_ip)
            like.delete()
        except Like.DoesNotExist:
            pass

        return redirect(f'/{pk}')


# Util methods
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
