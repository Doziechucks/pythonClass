def check_palindrome(word):
   for number in range(len(word)):
     if word[number] == word[-(number + 1)]:
        return "palindrome"
   else:
     return "not palindrome"
word = "madam"
print(check_palindrome(word))