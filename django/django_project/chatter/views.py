# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt

def getchatts(request):
    if request.method != 'GET':
        return HttpResponse(status=404)
    response = {}
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM chatts;')
    rows = cursor.fetchall()
    response['chatts'] = rows
    return JsonResponse(response)

@csrf_exempt
def addchatt(request):
    if request.method != 'POST':
        return HttpResponse(status=404)
    json_data = json.loads(request.body)
    username = json_data['username']
    message = json_data['message']
    cursor = connection.cursor()
    cursor.execute('INSERT INTO chatts (username,message) VALUES ' '(%s,%s);', (username,message))
    return JsonResponse({})

@csrf_exempt
def adduser(request):
    if request.method != 'POST':
        return HttpResponse(status=404)
    json_data = json.loads(request.body)
    username = json_data['username']
    email = json_data['email']
    name = json_data['name']
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, name, email) VALUES ' '(%s, %s, %s);', (username, name, email))
    return JsonResponse({})


# Create your views here.
