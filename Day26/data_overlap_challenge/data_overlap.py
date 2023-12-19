file_content1 = []
file_content2 = []

with open('file1.txt') as f:
    for line in f:
        strip_line = line.strip()
        file_content1.append(int(strip_line))

with open('file2.txt') as f:
    for line in f:
        strip_line = line.strip()
        file_content2.append(int(strip_line))

result = []

for i in file_content1:
    if i in file_content2:
        result.append(i)

print(result)
