my_ip = input("Enter an IPv4 Address: ")

my_ipv4 = str.split(my_ip, '.')
for i in my_ipv4:
    print(f"{i:<12}")