file = open("./nums.txt", 'w')

for i in range(1, 46340):
    file.write(str(i*i) + '\n')