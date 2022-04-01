# flag = input("String: ")
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"

# FIRST_CHAR = "p"
# LAST_CHAR = "}"


def encrypt(flag):
    flag_enc = ""
    for i in range(0, len(flag), 2):
        flag_enc += ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1]))])
    print(flag_enc)
    return flag_enc


def decrypt(flag):
    for char in flag:
        for i in range(0, 127):
            if 126 >= ord(char) - (i << 8) >= 0:
                print(chr(i) + chr(ord(char) - (i << 8)), end='')


decrypt(flag)
