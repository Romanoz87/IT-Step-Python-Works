striqoni = input("Enter Some text: ").lower()
striqoni = striqoni.strip()
print(striqoni)
if "python" in striqoni:
    striqoni = striqoni.replace("python", "Python")
    print(striqoni)
