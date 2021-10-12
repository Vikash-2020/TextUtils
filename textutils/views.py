# I have created this file -Vikash Sahni
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {"name": "Vikash Sahni", "age": "21", "Reg": "19MIM10065"}
    return HttpResponse(render(request, 'index.html', params))


def analyze(request):
    getText = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capsAll = request.POST.get('capsAll', 'off')
    charCounter = request.POST.get('charCounter', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
    removedPunc = ''
    upperCase = ''
    charCount = ''
    removeNewLine = ''
    extraSpaceRemove = ''
    count = 0
    
    if removepunc == 'on':
        punctutations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ''
        for char in getText:
            if char not in punctutations:
                analyzed = analyzed + char
        getText = analyzed
        removedPunc = "Punctutations Removed"
    
    if capsAll == "on":
        getText = getText.upper()
        upperCase = "UPPER CASED"

    if charCounter == "on":
        count = len(getText)
        charCount = "Character Counted"

    if newLineRemover == "on":
        analyzed = ''
        for char in getText:
            if char != '\n' and char != '\r':
                analyzed += char
        getText = analyzed
        removeNewLine = "New line removed"

    if extraSpaceRemover == "on":
        analyzed = ''
        for i,char in enumerate(getText):
            if not (getText[i] == " " and getText[i+1] == " "):
                analyzed += char
        getText = analyzed
        extraSpaceRemove = "Extra space removed"
    

    if removepunc == "off" == capsAll == charCount:
        return HttpResponse('Error')
        
    param1 = {'purpose': " ".join([removedPunc,upperCase,charCount,removeNewLine,extraSpaceRemove]), 'analyzedText': getText, 'Count': count}
    return HttpResponse(render(request, 'analyze.html', param1))
