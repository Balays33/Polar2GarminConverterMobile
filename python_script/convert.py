import os

import re



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
    print(myPolarstring)
    # Replace 'start_word' and 'end_word' with your actual words
    new_text = remove_between_words(myPolarstring, start_word_1, end_word_1)
    Garmin_text = remove_between_words(new_text, start_word_2, end_word_2)
    print(Garmin_text)

def remove_between_words(Polarstring, start_word, end_word):
    print(Polarstring)
    pattern = r"(?<=%s)(.*?)(?=%s)" % (start_word, end_word)
    print(pattern)
    return re.sub(pattern, "", Polarstring)




