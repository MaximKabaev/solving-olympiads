value = "ESVNMCW"
value_list = []
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
for i in range(len(value)):
    value_list.append(value[i])


def decrypt(i):
    _sum = 0
    first_num = 0

    for a in range(len(letters)):
        if value_list[i] == letters[a]:
            first_num = a
        if value_list[i + 1] == letters[a]:
            _sum = a
    second_num = _sum - first_num
    if second_num < 0:
        second_num += 25
    second_letter = letters[second_num]
    value_list[i + 1] = second_letter


for i in range(0, len(value_list) - 1, 2):
    # print(value_list[i])
    decrypt(i)
print(value_list)
if len(value_list) % 2 != 0:
    print('lol')
    decrypt(len(value_list) - 2)

print(value_list)
