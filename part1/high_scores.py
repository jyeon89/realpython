import csv
import os

# path varies depend on your file location
my_path = "C:/Users/Jae/Desktop/book1-exercises/chp09/practice_files"

high_scores_dict = {}
with open(os.path.join(my_path, "scores.csv"), "r") as my_file:
    file_reader = csv.reader(my_file)
    for name, score in file_reader:
        score = int(score)
        if name in high_scores_dict:
            if score > high_scores_dict[name]:
                high_scores_dict[name] = score
        else:
            high_scores_dict[name] = score

for name in sorted(high_scores_dict):
    print(name, high_scores_dict[name])
