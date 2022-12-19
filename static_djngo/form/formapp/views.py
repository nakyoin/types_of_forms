from django.shortcuts import render

def index(request):
    data = {"head_text_first" : "First Post", "text_first" : "Text of my First Post", "head_text_sec" : "Second Post", "text_sec" : "Text of my Second Post", "head_text_third" : "Third Post", "text_third" : "Text of my Third Post"}
    return render(request, "index.html", context=data)