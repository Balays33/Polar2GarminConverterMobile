from django.shortcuts import render
from django.http import HttpResponse
from python_script import convert

import os
from django.conf import settings

from django.core.files.storage import FileSystemStorage

# Create your views here.

"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print("upload file name: {}".format(myfile.name))
        print("upload file size: {}".format(myfile.size))

        # Read the file contents line by line
        """
        with myfile.open('rb') as f:
            for line in f:
                print(line)
        """

        #convert.test(myfile)
        if convert.filename_extension_Checker(myfile) == True:
            convert.search_file(myfile,'<Creator', '</Creator>', '<Author', '</Author>')

        #saved_New_Polar_file_url = open(os.path.join(settings.BASE_DIR, 'templates/download/Garmin-Ready-file.TCX'))
        #print(saved_New_Polar_file_url)


        #saved_New_Polar_file_url = "http://127.0.0.1:8000/" + 'templates/download/Garmin-Ready-file.TCX'
        saved_New_Polar_file_url = "balays33.pythonanywhere.com/" + 'templates/download/Garmin-Ready-file.TCX'

        print("saved_New_Polar_file_url: " + saved_New_Polar_file_url)

        return render(request, 'Polar2GarminC/index.html', {

            'saved_New_Polar_file_url': saved_New_Polar_file_url
        })

    return render(request, 'Polar2GarminC/index.html', context={'hello': 'world'})

def test(request):
    print("Work Test")
    saved_New_Polar_file_url = "http://127.0.0.1:8000/"+'templates/download/Garmin-Ready-file.TCX'
    print(saved_New_Polar_file_url)
    print(open(os.path.join(settings.BASE_DIR, 'templates/download/Garmin-Ready-file.TCX')))
    context = {
        'posts': posts,
        'saved_New_Polar_file_url': saved_New_Polar_file_url
    }
    return render(request, 'Polar2GarminC/test.html', context)



