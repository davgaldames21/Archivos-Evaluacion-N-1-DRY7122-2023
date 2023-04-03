aclnum = int(input("¿Cual es el numero de la ACL Ipv4?: "))


print(aclnum)

if aclnum >= 1 and aclnum <= 99:
    print("Esta es una ACL Ipv4 Estandar")

elif aclnum >= 100 and aclnum <= 199:
    print("Esta es una ACL Ipv4 Extendida")

else:
    print("Esto no es una ACL Ipv4 Estandar ni Extendida")
