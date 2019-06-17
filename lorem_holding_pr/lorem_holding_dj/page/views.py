from django.shortcuts import render
# from django.http import HttpResponse


def home_page(request):
    data = {}
    names = [
        "hakan",
        "enes",
        "sezer",
        "mihrace",
        "oktay",
        "pinarx2",
        "mervan",
        "emran",
    ]
    
    if "hatice" in names:
        names.remove("hatice")

    new_name_list = []

    for item in names:
        if item != "hakan":
            new_name_list.append(item)

    data['names'] = names
    # data['names'] = new_name_list

    print("x" * 20)
    print("Home Page View Calisiyor")
    print(data)
    print("x" * 20)
    # return HttpResponse("Ana Sayfa")  # Simple Html Response
    return render(request, "page/home.html", data)

def about_us(request):
    data = {}
    return render(request, "page/about_us.html", data)

def contact(request):
    data = {}
    return render(request, "page/contact.html", data)


