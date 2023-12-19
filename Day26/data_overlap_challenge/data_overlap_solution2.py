with open('file1.txt') as f:
    file_content1 = f.readlines()

with open('file2.txt') as f:
    file_content2 = f.readlines()

result = [int(i) for i in file_content1 if i in file_content2]
print(result)
