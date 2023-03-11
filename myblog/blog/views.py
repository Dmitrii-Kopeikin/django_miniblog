from django.shortcuts import render
from django.views.generic.base import View
from .models import Publication


# noinspection PyMethodMayBeStatic
class PublicationView(View):
    """Publications view"""

    def get(self, request):
        """

        :param request:
        :return:
        """
        publications = Publication.objects.all()

        return render(request, 'blog/blog.html', {'publication_list': publications})
