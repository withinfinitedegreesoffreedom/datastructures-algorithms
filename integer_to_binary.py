from stack import Stack

def int_to_bin(dec_num):
    s = Stack()

    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.isEmpty():
        bin_num = bin_num + str(s.pop())

    return bin_num


print(int_to_bin(242))
print(int_to_bin(2005))
