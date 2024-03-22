FILENAME = "file_question.txt"
in_file = open(FILENAME)
for line in in_file:
    parts = line.strip().split(",")
    print(parts[0])
in_file.close()

#SIMILAR QUESTIONS IN THE FINAL EXAM