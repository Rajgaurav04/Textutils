# This is created bu me ~ Raj Gaurav
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def textfunc(request):

    # Fetching Data from Form

    djtext = request.POST.get('text', 'default')
    checkpunc = request.POST.get('checkpunc', 'off')
    checkextraspace = request.POST.get('checkex', 'off')
    checkcount = request.POST.get("checkcount", "off")
    checknewline = request.POST.get("checkln", "off")
    upper = request.POST.get('upper', 'off')
    allcaps = request.POST.get('allcaps', 'off')

    # Appending Purpose
    purpose = ""
    analyzed = djtext

    # Checking for all checkboxes either it is on or not

    if checkpunc == "on":
        mytext = ''
        punctuations = '''!()-[];:{'",<>}./?@#$%^&*_~'''
        for char in analyzed:
            if char not in punctuations:
                mytext = mytext + char
        analyzed = mytext
        purpose = "Remove Punctuation"

    if checkextraspace == "on":
        mytext = ""
        for index, char in enumerate(analyzed):
            if not (analyzed[index] == " " and analyzed[index + 1] == " "):
                mytext = mytext + char
        purpose += "| Remove Extra Space"
        analyzed = mytext

    if checkcount == "on":
        text = djtext.split()
        lencount = f"Total Words : {len(text)}"
        purpose += "| Count Words"

    elif checkcount == "off":
        lencount = ""

    if checknewline == "on":
        mytext = ""
        for char in analyzed:
            if char != "\n" and char != "\r":
                mytext = mytext + char
        analyzed = mytext
        purpose += "| Remove New line"

    if upper == "on":
        analyzed = analyzed.upper()
        purpose += "| UPPER CASE"

    if allcaps == "on":
        analyzed = analyzed.title()
        purpose += "| All words Capitalize"

    # If no any checkbox is selected
    if (checkpunc != "on" and checkcount != "on" and checkextraspace != "on" and checknewline != "on" and upper != "on" and allcaps != "on"):
        return HttpResponse("Error! Please Try again ")

    # Finalizing the result --------- >>>  What is Purpose , what is lencount, what is analyzed text
    params = {"purpose": purpose, "analyzed": analyzed, "charcount": lencount}

    # Returning the data(params) to textfunc.html
    return render(request, 'textfunc.html', params)
