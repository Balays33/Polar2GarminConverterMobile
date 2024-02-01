from django.shortcuts import render
from django.http import HttpResponse
from python_script import convert

import os

# Create your views here.

"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

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


    return render(request, 'Polar2GarminC/index.html', context={'hello': 'world'})



