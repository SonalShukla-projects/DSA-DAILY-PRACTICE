def binary_octal(binary_str:str)->str:
    remainder=len(binary_str)%3
    if remainder!=0:
        binary_str=("0"*(3-remainder))+binary_str
    octal_digits=[]

    for i in range (0,len(binary_str),3):
        chunk=binary_str[i:i+3]
        octal_val=(int(chunk[0])*4+int(chunk[1])*2+int(chunk[2])*1)
        octal_digits.append(str(octal_val))
    return "".join(octal_digits)

if __name__=="__main__":
    binary_input=input().strip()
    print(binary_octal(binary_input))