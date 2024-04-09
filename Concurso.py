i = int(input("Numero"))
print(f"{i} -> ", end="")
while i!=1:
    if i%2==0:
        i=i//2
        print(f"{i} -> ",end="")
    else:
        i=(i*3)+1
        print(f"{i} -> ",end="")