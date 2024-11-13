#    ტექსტი ვალიდურია თუ შეიცავს მხოლოდ ციფრებს და რიცხვებს
import re
striqoni = input("input text: ")
pattern = r"^[A-Za-z0-9]+$"
if re.match(pattern, striqoni):
    print("valid")
else:
    print("not valid")