import re

import os
from django.core.files.storage import FileSystemStorage
import sys




def test(testfile):
    print("This is a test function")
    print(testfile.size)
    with testfile.open('rb') as f:
        for line in f:
            print(line)





def search_file(file, start_word_1, end_word_1, start_word_2, end_word_2):
    print("searching the file {} , {} , {} , {}".format(start_word_1, end_word_1, start_word_2, end_word_2))
    myfile = file
    # Check if the file path exists
    if not myfile:
        print("Error: File not found:", myfile)
        return
    myPolarstring = ''
    Garmin_text = ''
    with myfile.open('rb') as f:
        for line in f:
            myPolarstring = line.decode('utf-8')
    #print(myPolarstring)
    # Replace 'start_word' and 'end_word' with your actual words
    new_text = remove_between_words(myPolarstring, start_word_1, end_word_1)
    Garmin_text = remove_between_words(new_text, start_word_2, end_word_2)
    file_write(Garmin_text)
    """
    returned_file_save = 
    filesystem = FileSystemStorage()
    filename = filesystem.save(returned_file_save.name, returned_file_save)
    saved_New_Polar_file_url = filesystem.url(filename)
    print("new Polar file name:" + filename)
    print("saved_New_Polar_file_url: " + saved_New_Polar_file_url)
    """
    #print(Garmin_text)



def remove_between_words(Polarstring, start_word, end_word):
    #print(Polarstring)
    pattern = r"(?<=%s)(.*?)(?=%s)" % (start_word, end_word)
    #print(pattern)
    return re.sub(pattern, "", Polarstring)

def file_write(updateinfo):
    f = open("templates/download/Garmin-Ready-file.TCX", "w")
    f.write(updateinfo)
    f.close()

    # open and read the file after the overwriting:
    #f = open("templates/download/Garmin-Ready-file.TCX", "r")
    #print(f.read())
    return f


def filename_extension_Checker(myfile):
    print("Filename extension checker running")
    suffix = "tcx";
    result = myfile.name.lower().endswith(suffix)
    print("The upload file is TCX file:", result)
    if result == True:
        return result




