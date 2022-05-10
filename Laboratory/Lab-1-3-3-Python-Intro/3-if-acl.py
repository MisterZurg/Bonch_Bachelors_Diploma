aclNum = int(input("Какой номер ACL IPv4? "))
if aclNum >= 1 and aclNum <= 99:
    print("Это стандартный ACL IPv4.")
elif aclNum >=100 and aclNum <= 199:
    print("Это расширенный ACL IPv4.")
else:
    print("Это ни стандартный и ни расширенный IPv4 ACL.")
