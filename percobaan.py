f = open("data.txt", "r")
content = f.read()


content_list = content.splitlines()
f.close()
print(content_list)