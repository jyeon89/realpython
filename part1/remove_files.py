import os

my_path = "C:/Users/Jae/Desktop/book1-exercises/chp09/practice_files/little pics"

for folder, subfolders, files in os.walk(my_path):
    for file in files:
        join_path = os.path.join(folder, file)

        jpg = file.lower().endswith(".jpg")

        size = os.path.getsize(join_path)

        if jpg and size<2000:
            print("Deleteing: {}:".format(file))
            os.remove(join_path)
