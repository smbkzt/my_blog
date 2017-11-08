import urllib.request
import urllib.parse
import requests
from lxml import html

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import Http404

from .models import Pocket


def index(request):
    if request.method == "GET":
        all_links = Pocket.objects.all()
        pagination = Paginator(all_links, 10)
        page = request.GET.get('page')
        try:
            latest_links = pagination.page(page)
        except PageNotAnInteger:
            latest_links = pagination.page(1)
        except EmptyPage:
            latest_links = pagination.page(pagination.num_pages)

        context = {
            "latest_links": latest_links,
        }
        return render(request, "pocket/my-pocket.html", context)


def url_add(request):
    if request.method == "POST":
        url = request.POST['url']
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        resp = requests.get(url)
        raw_par = html.fromstring(resp.content)
        # paragraphs = re.findall(r'<p>(.*?)<p>', str(respData))
        # print(paragraphs)
        # for par in paragraphs:
        #     par = par + "<br/>"
        #     raw_par += par

        # raw_par.replace(r"\n", "<br/>")

        print(raw_par)

        new_pocket = Pocket(title="test",
                            url=url,
                            paragraph=raw_par,
                            user=request.user)
        new_pocket.save()

        return redirect("pocket:index")
    else:
        raise Http404()
