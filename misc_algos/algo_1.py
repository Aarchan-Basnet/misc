# given name of animals separated by a hyphen, find the length of last animal.

s = "Elephant-Tiger-Lion--"

temp = s.split('-')
# print(len(temp[-1]))

while len(temp[-1]) == 0:
    temp.pop()
print(len(temp[-1]))
