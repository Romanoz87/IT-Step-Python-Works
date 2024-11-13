# ტელეფონის ნომრის ვალიდურობს შემოწმება
import re

phone_num = input("enter phone number")

pattern = r"\([0-9]{3}\) [0-9]{3}-[0-9]{3}"

if re.fullmatch(pattern, phone_num):
    print(phone_num)
else:
    print("Not Matched")



 
  