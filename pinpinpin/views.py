from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.parsers import JSONParser
import json
import requests
from django.urls import reverse
from pinpinpin import models
from rest_framework import serializers

class InformationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    openid = serializers.CharField()
    gotime = serializers.CharField()
    departure = serializers.CharField()
    destination = serializers.CharField()
    goal = serializers.CharField()
    telephone=serializers.CharField()
    peoplenum=serializers.CharField()
    sortgotime=serializers.IntegerField()

class UserSerializer(serializers.Serializer):
    openid = serializers.CharField()
    telephone=serializers.CharField()




class OpenidUtils(object):
    def __init__(self, jscode):
        self.url = "https://api.weixin.qq.com/sns/jscode2session"
        self.appid = "wx8a41e8214258a086"
        self.secret = "5a2bb1f6b87a7e23d4599e145856f6f0"
        self.jscode = jscode  # 前端传回的动态jscode

    def get_openid(self):
        url = self.url + "?appid=" + self.appid + "&secret=" + self.secret + "&js_code=" + self.jscode + "&grant_type=authorization_code"
        r = requests.get(url)
        #openid = r.json()['openid']
        openid = r.json().get('openid', '')
        errcode = r.json().get('errcode','')
        errmsg = r.json().get('errmsg','')
        return openid,errcode,errmsg

class PinUserLoginView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        r = OpenidUtils(request.data['code'])
        ret = r.get_openid()
        print(ret)
        return HttpResponse(ret, content_type="application/json")

class SubmitView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        obj = models.PinInformation(openid=request.data['openid'],gotime=request.data['gotime'],
                                    departure=request.data['departure'],
                                    destination=request.data['destination'],
                                    goal=request.data['goal'],telephone=request.data['telephone'],peoplenum=request.data['peoplenum'],sortgotime=request.data['sortgotime'])
        obj.save()
        return HttpResponse('success')

class MyinfoView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        k= models.PinInformation.objects.filter(openid=request.data['openid'])
        myinfo= k.order_by('-sortgotime')
        ser = InformationSerializer(instance=myinfo, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(ret)
        return HttpResponse(ret, content_type="application/json")

class InformationsView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        informations = models.PinInformation.objects.order_by('-id')[:10]
        ser = InformationSerializer(instance=informations,many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(ret)
        return HttpResponse(ret, content_type="application/json")

class DeleteView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        models.PinInformation.objects.filter(id=request.data['id']).delete()
        return HttpResponse('success')

class SaveUserView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models.PinUser.objects.filter(openid=request.data['openid'])
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
class IsUserView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models.PinUser.objects.filter(openid=request.data['openid'])


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
            return HttpResponse(0)

class UserInfoView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # r = OpenidUtils(request.data['code'])
        # ret = r.get_openid()
        # ret=request.data['openid']
        k = models.PinUser.objects.filter(openid=request.data['openid'])
        print(k)
        if k:
            print('已经存在')
            models.PinUser.objects.filter(openid=request.data['openid']).update(telephone=request.data['telephone'])
            return HttpResponse('sucessedit')
        else:
            obj = models.PinUser(openid=request.data['openid'], telephone=request.data['telephone'])
            obj.save()
            return HttpResponse('sucessinsert')
class SortView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        # models.PinUser.objects.order_by('openid')
        # models.PinInformation.objects.order_by('openid') and


        informations = models.PinInformation.objects.filter(sortgotime__range=[request.data['sortgotime'], 9999999])
        k=informations .order_by('sortgotime')


        ser = InformationSerializer(instance=k, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)  # False之后就可以输出中文了
        print(ret)
        return HttpResponse(ret, content_type="application/json")











