import os
from django.core.files.storage import FileSystemStorage

updatedNewFile = ""


def search_str(file_path, start_word_1, end_word_1, start_word_2, end_word_2):
    try:
        with open("./"+file_path, 'r', encoding='utf-8') as fp:
            for l_no, line in enumerate(fp):
                # search string
                if start_word_1 in line and end_word_1 in line:
                    print(f'{start_word_1} and {end_word_1} found in a file')
                    print('Line Number:', l_no)
                    print('Text Between:', line[line.find(start_word_1):line.find(end_word_1) + len(end_word_1)])
                if start_word_2 in line and end_word_2 in line:
                    print(f'{start_word_2} and {end_word_2} found in a file')
                    print('Line Number:', l_no)
                    print('Text Between:', line[line.find(start_word_2):line.find(end_word_2) + len(end_word_2)])
                    # create new file
                    returned_file_save = copymodifyFile(line, start_word_1, end_word_1, start_word_2, end_word_2)
        print("search_sr is done")
        filesystem = FileSystemStorage()
        filename = filesystem.save(returned_file_save.name, returned_file_save)
        saved_New_Polar_file_url = filesystem.url(filename)
        print("new Polar file name:" + filename)
        print("saved_New_Polar_file_url: " + saved_New_Polar_file_url)
    except FileNotFoundError:
        print(f'File {file_path} does not exist.')
    return saved_New_Polar_file_url



def copymodifyFile(line,start_word_1, end_word_1, start_word_2, end_word_2):
    with open('new_file.TCX', 'w', encoding='utf-8') as new_file:
        new_file.truncate(0)
        start_index = line.find(start_word_1)
        end_index = line.find(end_word_1) + len(end_word_1)
        new_line = line[:start_index] + line[end_index:]
        start_index = new_line.find(start_word_2)
        end_index = new_line.find(end_word_2) + len(end_word_2)
        new_file.write(new_line[:start_index] + new_line[end_index:])
    # open and read the file after the overwriting:
    f = open("new_file.TCX", "r")
    #print(f.read())
    print("the new garmin ready file was created")
    #return "job done"
    return f

def test(testfile):
    print("This is a test function")
    print(testfile.size)
    with testfile.open('rb') as f:
        for line in f:
            print(line)





def search_file(file, start_word_1, end_word_1, start_word_2, end_word_2):
    print("function search file '<Creator', '</Creator>', '<Author', '</Author>'")
    myfile = str.file
    # Check if the file path exists
    if not os.path.exists(myfile):
        print("Error: File not found:", myfile)
        return

    # Open the file in binary mode
    try:
        with myfile.open('rb') as f:
            # Iterate over each line of the file
            for l_no, line in enumerate(f):
                # Search for the keywords
                if start_word_1 in line and end_word_1 in line:
                    print(f'{start_word_1} and {end_word_1} found in a file')
                    print('Line Number:', l_no)
                    print('Text Between:', line[line.find(start_word_1):line.find(end_word_1) + len(end_word_1)])

                if start_word_2 in line and end_word_2 in line:
                    print(f'{start_word_2} and {end_word_2} found in a file')
                    print('Line Number:', l_no)
                    print('Text Between:', line[line.find(start_word_2):line.find(end_word_2) + len(end_word_2)])
    except FileNotFoundError as e:
        print("Error:", e)
        print("Error opening file:", myfile)
    print("search_sr is done")

