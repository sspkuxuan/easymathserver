#!/usr/bin/env python
#coding:utf-8
  
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easymath.settings")
  
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
  
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
  
  
def main():
    from api.models import QuestionLib
    f = open('4down.txt')
    for line in f:
        grade,question,choiceA,choiceB,choiceC,choiceD,answer = line.split('****')
        #obj = QuestionLib(grade=grade,question=question,choiceA=choiceA,choiceB=choiceB,choiceC=choiceC,choiceD=choiceD,answer=answer)
        #obj.save()
        QuestionLib.objects.get_or_create(grade=grade,question=question,choiceA=choiceA,choiceB=choiceB,choiceC=choiceC,choiceD=choiceD,answer=answer)
    f.close()
  
if __name__ == "__main__":
    main()
    print('Done!')
    #格式有问题可以用NOTEPAD打开换编码格式为“以UTF8无BOM格式编码”
