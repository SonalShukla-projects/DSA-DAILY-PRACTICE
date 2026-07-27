def decimal_binary(n:int)->str:
    return bin(n)[2:]

if __name__=="__main__":
    num=int(input().strip())
    print(decimal_binary(num))