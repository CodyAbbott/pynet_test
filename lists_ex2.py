my_ip = input("Enter an IPv4 Address: ")

my_ipv4 = list(str.split(my_ip, '.'))

my_ipv4[-1] = 0

for octet in my_ipv4:
    my_num = int(octet)
    my_bin = bin(my_num)
    print(str(my_num) + "   " + str(my_bin))
    
