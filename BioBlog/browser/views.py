import os
from re import I
from bioblog.settings import STATICFILES_DIRS
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from .function.function import home_loading, manage_loading, self_information, search_paper, idEditor, getYearList

# Create your views here.
class home_page(View):
    def get(self, request):
        data = {'data':home_loading(), 'information':self_information()}
        return render(request, 'browser/index.html', data)

class artical_page(View):
    def get(self, request):
        paper_id = request.GET.get('id')
        paper_data = idEditor().search(paper_id)
        title = paper_data["title"]
        author = paper_data["author"]
        stamp = paper_data["stamp"]
        date = paper_data["date"]
        with open(os.path.join(STATICFILES_DIRS[0], 'browser/uploads/'+paper_id+'.md'), 'r', encoding='utf-8') as f:
            content = f.read().replace('\n', '&hhf;').replace('\\', '/')
        data = {'paper_id':paper_id, 'title':title, 'author':author, 'stamp':stamp, 'date':date, 'content':content, 'information':self_information()}
        return render(request, 'browser/artical.html', data)

class writer_page(View):
    def get(self, request):
        return render(request, 'browser/writer.html')

class login_page(View):
    def get(self, request):
        return render(request, 'browser/login.html')

class manage_page(View):
    def get(self, request):
        date_list, result_list = getYearList()
        data = {'data':manage_loading(), 'information':self_information(), 'date_list':date_list, 'color_list':result_list}
        return render(request, 'browser/manage.html', data)

class login_page_function_login(View):
    def post(self, request):
        name = request.POST.get('login_name')
        pwd = request.POST.get('login_pwd')
        if name == 'Jarry' and pwd == '123456':
            response = HttpResponseRedirect(reverse('home_page'))
            response.set_cookie('username',name,3600)
            return response
        else:
            return HttpResponseRedirect(reverse('login_page'))

class login_page_function_signout(View):
    def get(self, request):
        response = HttpResponseRedirect(reverse('home_page'))
        response.set_cookie('username','',1)
        return response

class write_page_function_upload(View):
    def post(self, request):
        content = request.POST.get('my-editormd-markdown-doc')
        title = request.POST.get('artical_title')
        abstract = request.POST.get('artical_abstract')
        image = request.POST.get('artical_image')
        date = request.POST.get('artical_date')
        stamp = request.POST.get('artical_stamp')
        author = '梁雨朝'
        idEditor().write(title, author, stamp, date, abstract, image, content)
        idEditor().im_write(paper=1)
        return HttpResponseRedirect(reverse('home_page'))

class home_page_function_search(View):
    def get(self, request):
        key = request.GET.get('artical_searchBar')
        data = {'data':search_paper(key), 'information':self_information()}
        return render(request, 'browser/index.html', data)

class artical_page_function_good(View):
    def get(self, request):
        paper_id = request.GET.get('paper')
        prefer = request.GET.get('prefer')
        idEditor().edit(paper_id, prefer)
        idEditor().im_write(good=int(prefer))
        return HttpResponseRedirect(reverse('artical_page')+"?id="+paper_id)

class manage_page_function_information(View):
    def post(self, request):
        author = request.POST.get('user_card_detail_author')
        detail = request.POST.get('user_card_detail_detail')
        like_list_1 = request.POST.get('user_like_list_1')
        like_list_2 = request.POST.get('user_like_list_2')
        like_list_3 = request.POST.get('user_like_list_3')
        like_list_4 = request.POST.get('user_like_list_4')
        like_list_5 = request.POST.get('user_like_list_5')
        like = ''
        for i in [like_list_1, like_list_2, like_list_3, like_list_4, like_list_5]:
            if i != '':
                like += '&' + i
        if like == '':
            for key in idEditor().get_idList():
                like = '&' + key
                break
        idEditor().im_write(author=author, detail=detail, like=like[1:])
        return HttpResponseRedirect(reverse('manage_page'))

class manage_page_function_delete(View):
    def get(self, request):
        paper_id = request.GET.get('id')
        good = idEditor().delete(paper_id)
        like = idEditor().get_imList()["like"]
        if paper_id in like:
            like.remove(paper_id)
        like = '&'.join(like)
        idEditor().im_write(paper=int(-1), good=-int(good), like=like)
        return HttpResponseRedirect(reverse('manage_page'))