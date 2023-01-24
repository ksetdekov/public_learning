list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


inputnum_list = []
while True:
    value_given = input("enter number")
    if value_given == '':
        output = [list1[letter_position] for letter_position in inputnum_list]
        print(''.join(output))
        inputnum_list = []
        continue
    inputnum_list.append(int(value_given))
