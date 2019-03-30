# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,User,s_b,Order
from django.db.models import Q
from django.contrib.auth import authenticate
from django.shortcuts import render,render_to_response
from django import forms
from django.db import models
from django.forms import ModelForm
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
import json
import datetime,calendar
import time
from operator import attrgetter
def welcome(request):
    test_user = User.objects.filter(username='test1')
    return render(request,'welcome.html',{'test_user':test_user})

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            nickname = uf.cleaned_data['nickname']
            college = uf.cleaned_data['college']
            major = uf.cleaned_data['major']
            campus = uf.cleaned_data['campus']
            grade = uf.cleaned_data['grade']
            User.objects.create(username=username,
                                password=password,
                                nickname=nickname,
                                image="timg.jpg",
                                college=college,
                                major=major,
                                campus=campus,
                                in_year=grade,
                                )
            return render(request, 'success.html')
        else:
            return render(request, 'register2.html')
    elif request.method == 'GET':
        return render(request, 'register2.html')


def login(request):
    if request.method =='POST':
        uf = UserFormLogin(request.POST)
        #user_name = request.POST.get('username','')
        #pass_word = request.POST.get('password','')
        #check_user= Users.objects.filter(username = user_name,password = pass_word)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username, password=password,state=0)
            # pdb.set_trace()
            if (len(userResult) > 0):
                response = HttpResponseRedirect('/web/home')
                response.set_cookie('username', username)
                return response
            else:
               return HttpResponse('no')
        else:
            return HttpResponse('no')
    elif request.method =='GET':
        return render(request,'login.html')

def home(request):
    value = request.COOKIES["username"]
    u=User.objects.filter(username=value,state=0)
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    if request.method =='POST':
        uf = HomeForm(request.POST)
        if uf.is_valid():
            search_book = uf.cleaned_data['search']
            response = HttpResponseRedirect('book_result/?b_name='+str(search_book))
 #           response.set_cookie('search_book', search_book)
            return response
        else:
            return HttpResponse('no input')
    elif request.method =='GET':
        return render(request,'home.html',{'user':nick})
def book_result(request):
    value = request.COOKIES["username"]
    search = request.GET.get('b_name')
    u = User.objects.filter(username=value, state=0)
    nick=u[0].nickname
    if request.method == 'POST':
        uf = BookResultForm(request.POST)
        if uf.is_valid():
            search_book = uf.cleaned_data['search']
            select=uf.cleaned_data['select']
            if search_book == "搜索课本":
                if select=='0':
                    search_Result = Book.objects.filter(state=0).exclude(seller=u).order_by('price')
                elif select=='1':
                    search_Result = Book.objects.filter(state=0).exclude(seller=u).order_by('-price')
                return render(request, 'book_result.html', {'user': nick, 'book': search_Result})

            if select=='0':
                search_Result = Book.objects.filter(bookname__contains=search_book, state=0).exclude(seller=u).order_by('price')
            elif select=='1':
                search_Result = Book.objects.filter(bookname__contains=search_book, state=0).exclude(seller=u).order_by('-price')
            return render(request, 'book_result.html', {'user': nick, 'book': search_Result})
        else:
            return HttpResponse('no input')
    elif request.method == 'GET':
        if search == "search book":
            search_Result = Book.objects.filter(state=0).exclude(seller=u).order_by('price')
            return render(request, 'book_result.html', {'user': nick, 'book': search_Result})
        search_Result = Book.objects.filter(bookname__contains=search, state=0).exclude(seller=u).order_by('price')
        return render(request, 'book_result.html', {'user': nick, 'book': search_Result})

def PCenter(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value,state=0)
    nick = userResult[0].nickname
    img = userResult[0].image
    description = userResult[0].description
    campus = userResult[0].campus

    college = userResult[0].college
    grade = userResult[0].in_year
    major = userResult[0].major
    contact=userResult[0].contact
    if request.method == 'POST':
        uf = PCenterForm(request.POST,request.FILES)
        if uf.is_valid():
            u_img = uf.cleaned_data['file']
            u_nick = uf.cleaned_data['nick_name']
            u_des = uf.cleaned_data['description']
            u_con=uf.cleaned_data['contact']
            obj=User.objects.get(username=value,state=0)
            obj.nickname=u_nick
            obj.image=u_img
            obj.description=u_des
            obj.contact=u_con
            obj.save()
            return render(request,'success_pc.html')

        elif uf.cleaned_data['nick_name'] and uf.cleaned_data['contact'] and uf.cleaned_data['description']:
            u_nick = uf.cleaned_data['nick_name']
            u_des = uf.cleaned_data['description']
            u_con = uf.cleaned_data['contact']
            o=User.objects.filter(username=value,state=0)
            o=o[0]
            o.contact=u_con
            o.nickname=u_nick
            o.description=u_des
            o.save()
            return render(request, 'success_pc.html')

        else:
            return HttpResponse('修改失败')
    elif request.method == 'GET':
        order_s = Order.objects.filter(seller_id=value).exclude(comment='None').order_by('-c_time')

        order_b = Order.objects.filter(buyer_id=value).exclude(tobuyer_comment='None').order_by(
            '-tobuyer_c_time')
        len2 = len(order_b) + len(order_s)
        return render(request, 'PCenter.html', {'user': value, 'nick': nick, 'img': img,'description':description,'campus':campus,
                                                'grade':grade,'major':major,'college':college,
                                                'order_s': order_s,
                                                'order_b': order_b,
                                                'len2': len2,
                                                'contact':contact,
                                                })



def upload(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    if request.method == 'POST':
        uf = UploadForm(request.POST, request.FILES )

        if uf.is_valid():
            b_name = uf.cleaned_data['b_name']
            b_author = uf.cleaned_data['b_author']
            b_publisher = uf.cleaned_data['b_publisher']
            b_description = uf.cleaned_data['b_description']
            b_price = uf.cleaned_data['b_price']
            b_way =uf.cleaned_data['b_way']
            b_img=uf.cleaned_data['b_img']
            user=User.objects.filter(username=value)
            book = Book(bookname=b_name,
                        author=b_author,
                        publisher=b_publisher,
                        price=b_price,
                        description=b_description,
                        way=b_way,
                        picture=b_img,
                        seller=user[0],
                       )
            book.save()
            return render(request, 'success_upload.html')
        else:
            return render(request, 'upload.html', {'user': nick})
    elif request.method == 'GET':
        return render(request, 'upload.html', {'user': nick})

def selling(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    if request.method == 'POST':
        uf = SellingForm(request.POST)
        if uf.is_valid():
            search = uf.cleaned_data['search']
            if search=="搜索已上架的课本":
                user = User.objects.filter(username=value,state=0)
                books = Book.objects.filter(seller=user[0],state=0)
                if (len(books) > 0):
                    return render(request, 'selling.html', {'user': nick, 'book': books, })
                else:
                    return render(request, 'selling.html', {'user': nick})
            user = User.objects.filter(username=value,state=0)
            books = Book.objects.filter(seller=user[0],bookname__contains=search,state=0)
            if (len(books) > 0):
                return render(request, 'selling.html', {'user': nick, 'book': books, })
            else:
                return render(request, 'selling.html', {'user': nick})

    elif request.method == 'GET':
        user = User.objects.filter(username=value,state=0)
        books = Book.objects.filter(seller=user[0],state=0)
        if (len(books) > 0):
            return render(request, 'selling.html', {'user': nick, 'book': books, })
        else:
            return render(request, 'selling.html', {'user': nick})



def own_book(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id=request.GET.get('b')
    book = Book.objects.filter(id=b_id)
    return render(request,'own_book.html',{'user':nick,'book':book,})




def buyer_center(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    if request.method=='GET':
        b_id = request.GET.get('b')
        if(b_id != '-1'):
            o=Order.objects.filter(book_id=b_id,state=0)
            if(len(o)==0):
                book =Book.objects.filter(id=b_id)
                book=book[0]
                if(book.state==0):
                    Order.objects.create(seller_name = book.seller.nickname,
                                         seller_id=book.seller.username,
                                         buyer_id=userResult[0].username,
                                         buyer_name = nick,
                                         book_id=b_id,
                                         bookname = book.bookname,
                                         picture = book.picture,
                                         price = book.price,
                                         buyer_image=userResult[0].image,
                                         seller_image=book.seller.image,
                                         way=book.way,
                             )
                    book.state=1
                    book.save()
                else:
                    return render(request, 'failed.html')
            else:
                return render(request, 'failed.html')
    orders=Order.objects.filter(buyer_id=value,state=0)
    return render(request, 'buyer_center.html', {'user': nick,'u_id':value,'order':orders,})

def seller_center(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    orders=Order.objects.filter(seller_id=value,state=0)
    return render(request, 'seller_center.html', {'user': nick,'u_id':value,'order':orders})

def comment(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id = request.GET.get('b')
    u_id=request.GET.get('p')
    orders = Order.objects.filter(buyer_id=u_id,book_id=b_id,comment='None',state=0)

    if(len(orders)==0):
        return HttpResponse('你已评论过该订单！')
    o = orders[0]
    if request.method=='POST':
        cf=commentForm(request.POST)
        if cf.is_valid():
            com=cf.cleaned_data['comment']
            sc=cf.cleaned_data['score']
            an=cf.cleaned_data['anonymous']
            if(an=="匿名"):
                o.anonymous=an
            o.score=sc
            o.comment=com
            now=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            o.c_time=int(now)
            o.save()
            return render(request,'success_comment.html')
        else:
            return HttpResponse('no' + str(cf))
    else:
        return render(request,'comment.html',{'nick':nick,'order':orders[0]})
def tobuyer_comment(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id = request.GET.get('b')
    u_id=request.GET.get('p')
    orders = Order.objects.filter(seller_id=u_id,book_id=b_id,tobuyer_comment='None',state=0)

    if(len(orders)==0):
        return HttpResponse('你已评论过该订单！')
    o = orders[0]
    if request.method=='POST':
        cf=tobuyer_commentForm(request.POST)
        if cf.is_valid():
            com=cf.cleaned_data['comment']
            sc=cf.cleaned_data['score']
            an=cf.cleaned_data['anonymous']
            if(an=="匿名"):
                o.tobuyer_anonymous=an
            o.tobuyer_score=sc
            o.tobuyer_comment=com
            now=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

            o.tobuyer_c_time=int(now)
            o.save()
            return render(request,'success_tobuyer_comment.html')
        else:
            return HttpResponse('no'+str(cf))
    else:
        return render(request,'tobuyer_comment.html',{'nick':nick,'order':orders[0]})

def others_center(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    others_id = request.GET.get('b')
    others_user = User.objects.filter(username=others_id, state=0)
    book = Book.objects.filter(seller=others_user[0],state=0)
    b_len = len(book)

    order_s=Order.objects.filter(seller_id=others_id).exclude(comment='None').order_by('-c_time')

    order_b=Order.objects.filter(buyer_id=others_id).exclude(tobuyer_comment='None').order_by('-tobuyer_c_time')
    len2=len(order_b)+len(order_s)
    if request.method == 'POST':
        uf = OthersCenterForm(request.POST)
        if uf.is_valid():
            search_book = uf.cleaned_data['search']
            if search_book == "搜索TA发布的课本":
                return render(request, 'others_center.html',{'nick': nick, 'others': others_user[0], 'book': book, 'book_len': b_len,
                                                             'order_s': order_s,
                                                             'order_b': order_b,
                                                             'len': len2,
                                                             })

            search_Result = Book.objects.filter(seller=others_user[0],bookname__contains=search_book,state=0)
            s_len = len(search_Result)
            return render(request, 'others_center.html', {'nick': nick,'others': others_user[0], 'book': search_Result,'book_len': s_len,
                                                          'order_s': order_s,
                                                          'order_b': order_b,
                                                          'len': len2,
                                                          })
        else:
            return HttpResponse('no input')
    elif request.method == 'GET':
        return render(request, 'others_center.html',{'nick': nick, 'others': others_user[0], 'book': book, 'book_len': b_len,
                                                     'order_s': order_s,
                                                     'order_b': order_b,
                                                     'len': len2,
                                                     })


def book(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id=request.GET.get('b')
    book = Book.objects.filter(id=b_id)
    rela=s_b.objects.filter(book_id=b_id,user_id=value)
    if(len(rela)==0):
        s_b.objects.create(book_id=b_id,user_id=value,relation='0')
    rela=s_b.objects.filter(book_id=b_id,user_id=value)
    rela=rela[0]
    if(rela.relation=='0'):
        return render(request,'book_cal.html',{'user':nick,'book':book,'u_id':value,})
    else:
        return render(request,'book_col.html',{'user':nick,'book':book,'u_id':value,})

def book_col(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id=request.GET.get('b')
    book = Book.objects.filter(id=b_id)
    rela=s_b.objects.filter(book_id=b_id,user_id=value)
    if(rela[0].relation=='0'):
        r=rela[0]
        r.relation=value
        r.save()
    return render(request,'book_col.html',{'user':nick,'book':book,'u_id':value,})

def book_cal(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname
    b_id=request.GET.get('b')
    book = Book.objects.filter(id=b_id)
    rela=s_b.objects.filter(book_id=b_id,user_id=value)
    if(rela[0].relation!='0'):
        r=rela[0]
        r.relation='0'
        r.save()
    return render(request,'book_cal.html',{'user':nick,'book':book,'u_id':value,})

def favorites(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    nick = userResult[0].nickname

    col=s_b.objects.filter(user_id=value).exclude(relation='0')
    b_id=col.all().values_list('book_id')

    book=Book.objects.filter(id__in=b_id)
    return render(request,'favorites.html',{'user':nick,'book':book})

def success_return(request):
    value = request.COOKIES["username"]
    userResult = User.objects.filter(username=value, state=0)
    b_id=request.GET.get('b_id')
    o=Order.objects.filter(book_id=b_id,buyer_id=value,state=0)
    b=Book.objects.filter(id=b_id,state=1)
    o=o[0]
    b=b[0]
    o.state=1
    b.state=0
    o.save()
    b.save()
    return render(request,'success_return.html')



class UserFormLogin(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

#class UserForm(forms.Form):
#    bname = forms.CharField(label='bname')
#    bauthor = forms.CharField(label='bauthor')
#    bpublisher = forms.CharField(label='bpublisher')
#   bdescription = forms.CharField(label='bdescription')
#    bprice = forms.CharField(label='bprice')
#    bway = forms.CharField(label='bway')
#    bimg = forms.ImageField(label='bimg')
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    nickname = forms.CharField(label='nickname')
    college=forms.CharField(label='college')
    campus=forms.CharField(label='campus')
    major=forms.CharField(label='major')
    grade=forms.CharField(label='grade')

class HomeForm(forms.Form):
    search = forms.CharField(label='search')

class UploadForm(forms.Form):
    b_name = forms.CharField(label='b_name', max_length=100)
    b_author = forms.CharField(label='b_author', widget=forms.PasswordInput())
    b_publisher = forms.CharField(label='b_publisher')
    b_description = forms.CharField(label='b_description')
    b_price = forms.FloatField(label='b_price')
    b_way = forms.IntegerField(label='b_way')
    b_img = forms.ImageField(label='b_img')

class PCenterForm(forms.Form):
    file=forms.ImageField(label='file')
    nick_name=forms.CharField(label='nick_name')
    description=forms.CharField(label='description')
    contact=forms.CharField(label='contact')

class SellingForm(forms.Form):
    search=forms.CharField(label='search')

class BookResultForm(forms.Form):
    search = forms.CharField(label='search')
    select = forms.CharField(label='select')

class commentForm(forms.Form):
    comment = forms.CharField(label='comment')
    score = forms.IntegerField(label='score')
    anonymous = forms.BooleanField(label='anonymous')

class tobuyer_commentForm(forms.Form):
    comment = forms.CharField(label='comment')
    score = forms.IntegerField(label='score')
    anonymous = forms.BooleanField(label='anonymous')
class OthersCenterForm(forms.Form):
    search = forms.CharField(label='search')
