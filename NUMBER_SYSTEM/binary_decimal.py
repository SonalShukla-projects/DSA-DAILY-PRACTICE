def binary_to_decimal(binary_str:str)->int:
    decimal_val=0
    for bit in binary_str:
        decimal_val=decimal_val*2 + int(bit)
        print(decimal_val)
    return decimal_val
if __name__=="__main__":
    binary_input=input().strip()
    print(binary_to_decimal(binary_input))
