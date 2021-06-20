secure = (('a','@'),('k','^'),('s','$'),('h','#'),('i','!'))
def SecurePasswd(generate):
    for a,b in secure:
        generate = generate.replace(a , b)
    return generate
if __name__ == "__main__":
    generate = input("enter passwd")
    generate = SecurePasswd(generate)
    print(f"secured passwd is {generate}")