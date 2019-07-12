from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
#from rest_framework.request import Request
#from rest_framework.parsers import JSONParser
import json
#from django.urls import reverse
from api import models
from rest_framework import serializers
import requests


class QuestionsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    grade = serializers.IntegerField()
    question = serializers.CharField()
    choiceA = serializers.CharField()
    choiceB = serializers.CharField()
    choiceC = serializers.CharField()
    choiceD = serializers.CharField()
    answer = serializers.CharField()

class ErrorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    openid = serializers.CharField()
    questionid = serializers.IntegerField()
    useranswer = serializers.CharField()
    trueanswer = serializers.CharField()
    qs= serializers.CharField()
class UserSerializer(serializers.Serializer):
    openid = serializers.CharField()
    telephone=serializers.CharField()


	

class OpenidUtils(object):
    def __init__(self, jscode):
        self.url = "https://api.weixin.qq.com/sns/jscode2session"
        self.appid = "wx4fd71fc4c9ec64bd"
        self.secret = "0426553d27abaed96ef0e9a38f77c9dd"
        self.jscode = jscode  # 前端传回的动态jscode

    def get_openid(self):
        url = self.url + "?appid=" + self.appid + "&secret=" + self.secret + "&js_code=" + self.jscode + "&grant_type=authorization_code"
        r = requests.get(url)
        #openid = r.json()['openid']
        openid = r.json().get('openid', '')
        errcode = r.json().get('errcode','')
        errmsg = r.json().get('errmsg','')
        return openid,errcode,errmsg
class UserLoginView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        r = OpenidUtils(request.data['code'])
        ret=r.get_openid()

        print(ret)

        return HttpResponse(ret, content_type="application/json")

class QuestionsView(APIView):
   # parser_classes = [JSONParser,]
    def post(self,request,*args,**kwargs):
        print(request.data)
        #返回POST的年级的全部题目
        question = models.QuestionLib.objects.filter(grade=request.data['grade']).order_by('?')[:10]
        ser = QuestionsSerializer(instance=question, many=True)
        ret = json.dumps(ser.data,ensure_ascii=False) #False之后就可以输出中文了
        print(ret)
	
        #return JsonResponse(ret)#这里我改了源码，把safe=True,改成了False
		#return HttpResponse(ret)
        return HttpResponse(ret,content_type="application/json")
        #return HttpResponse('收到')



class ResultsView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        obj = models.ErrorT(openid=request.data['openid'],questionid=request.data['questionid'],useranswer=request.data['useranswer'],trueanswer=request.data['trueanswer'],qs=request.data['qs'])
        obj.save()
        return HttpResponse('success')

class ErrorinView(APIView):
    # parser_classes = [JSONParser,]
    def post(self, request, *args, **kwargs):
        print(request.data)
        # 返回POST的年级的全部题目
        error= models.ErrorT.objects.filter(openid=request.data['openid'])
        ser = ErrorSerializer(instance=error, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(ret)
        # return JsonResponse(ret)#这里我改了源码，把safe=True,改成了False
        # return HttpResponse(ret)
        return HttpResponse(ret, content_type="application/json")
        # return HttpResponse('收到')

class ErroroutView(APIView):
    # parser_classes = [JSONParser,]
    def post(self, request, *args, **kwargs):
        print(request.data)
        # 返回POST的年级的全部题目
        error= models.QuestionLib.objects.filter(id=request.data['id'])
        ser = QuestionsSerializer(instance=error, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(ret)
        # return JsonResponse(ret)#这里我改了源码，把safe=True,改成了False
        # return HttpResponse(ret)
        return HttpResponse(ret, content_type="application/json")
        # return HttpResponse('收到')
class UserInfoView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models. MathUser.objects.filter(openid=request.data['openid'])
        print(k)
        if k:
            print('已经存在')
            models. MathUser.objects.filter(openid=request.data['openid']).update(telephone=request.data['telephone'])
            return HttpResponse('sucessedit')
        else:
            obj = models. MathUser(openid=request.data['openid'], telephone=request.data['telephone'])
            obj.save()
            return HttpResponse('sucessinsert')
class UserInfoView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models. MathUser.objects.filter(openid=request.data['openid'])
        print(k)
        if k:
            print('已经存在')
            models. MathUser.objects.filter(openid=request.data['openid']).update(telephone=request.data['telephone'])
            return HttpResponse('sucessedit')
        else:
            obj = models. MathUser(openid=request.data['openid'], telephone=request.data['telephone'])
            obj.save()
            return HttpResponse('sucessinsert')
class SaveUserView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models.MathUser.objects.filter(openid=request.data['openid'])
        t=[{'openid':request.data['openid'],'telephone':"编辑我的手机号"}]
        t1=json.dumps(t, ensure_ascii=False)  # False之后就可以输出中文了

        kser = UserSerializer(instance=k, many=True)
        kret= json.dumps(kser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(kret)
        print(k)
        if k:
            print('已经存在')
            return HttpResponse(kret, content_type="application/json")
        else:
            # obj = models.PinUser(openid=request.data['openid'], telephone=request.data['telephone'])
            # obj.save()
            return HttpResponse(t1,content_type="application/json")

"""
    def get(self,request,*args,**kwargs):
        question = models.QuestionLib.objects.all().first()
        ser = QuestionsSerializer(instance=question,many=False)
        ret = json.dumps(ser.data)
        return HttpResponse(ret)
        #return ret
"""