with open('file1.txt') as f:
    file_content1 = [int(line.strip()) for line in f]

with open('file2.txt') as f:
    file_content2 = [int(line.strip()) for line in f]

result = [i for i in file_content1 if i in file_content2]
print(result)
