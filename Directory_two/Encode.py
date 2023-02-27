# s  c  o  u  t
#   19  3 15 21 20
#  + 1  9  3  9  1
#  ---------------
#   20 12 18 30 21
#
#    m  a  s  t  e  r  p  i  e  c  e
#   13  1 19 20  5 18 16  9  5  3  5
# +  1  9  3  9  1  9  3  9  1  9  3
#   --------------------------------
#   14 10 22 29  6 27 19 18  6  12 8
# Task
# Write a function that accepts str string and key number and returns an array of integers representing encoded str.
#
# Input / Output
# The str input string consists of lowercase characters only.
# The key input number is a positive integer.
#
# Example
# Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
# Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

def encode(message, key):
    base_dict = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        base_dict[alpha[i]] = i + 1
    key1 = []
    count = 0
    for i in range(len(message)):
        try:
            key1.append(int(str(key)[count]))
        except IndexError:
            count = 0
            key1.append(int(str(key)[count]))
        count += 1
    key2 = []
    for j in message:
        key2.append(base_dict[j])
    code = []
    for i in range(len(key2)):
        code.append(key2[i] + key1[i])
    print(code)


encode('kggwouzfpiwpjwelbnfxqffawanvcnpimkmqprowggzbow', '790262')