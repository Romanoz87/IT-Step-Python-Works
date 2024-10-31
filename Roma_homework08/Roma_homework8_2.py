# სიტყვების შედარება ანაგრამებზე


def anagram(str1, str2):
    sorted_str1 = sorted(list(str1))  # სტრიქონები გადაგვყავს ლისტებში და ვასორტირებთ
    sorted_str2 = sorted(list(str2))
    if sorted_str1 == sorted_str2:
        print("\nUser entered words are anagrams: \n", "=" * 20)
        
    else:
        print("\nUser entered words are not anagrams: \n", "=" * 20)

str1 = input("Enter first word:..")
str2 = input("Enter second word:...")
anagram(str1, str2)