from django.shortcuts import render
from django.http import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)
    template_name = 'blogging/list.html'

    # def list_view(self, request):
    #     published = self.queryset.exclude(published_date__exact=None)
    #     posts = published.order_by('-published_date')
    #     # template = loader.get_template('blogging/list.html')
    #     context = {'posts': posts}
    #     # body = template.render(context)
    #     # return HttpResponse(body, content_type="text/html")
    #     return render(request, 'list.html', context)


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    # def detail_view(self, request, post_id):
    #     published = Post.objects.exclude(published_date__exact=None)
    #     try:
    #         post = published.get(pk=post_id)
    #     except Post.DoesNotExist:
    #         raise Http404
    #     context = {'post': post}
    #     return render(request, 'blogging/detail.html', context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
