def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i + 2):
            print("* ", end="")
        print("\r")
n=5
pattern(n)

print("--------------------------------------------------------------------")

def pattern(n):
     for i in range(1, n+1):
        for j in range(1, i + 2):
           
            print("* ", end="")
        print(" ")
n=5
pattern(n)






a="shreyas"
for i in a:
    print(i)
print("length of string is:",len(a),max(a),min(a))



b="my name is Shreyas"

print(b.upper())
print(b.lower())






a='''shreyas 
devadiga'''
print(a[0:7])

print(a.replace("i","e"))



txt="my name is \"punith\" gowda"
print(txt)




