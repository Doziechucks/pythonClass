def get_consonant_list(list):
   return[get_consonant(word) for word in list]

def get_consonant(word):
   vowel = "AEIOU"
   result = ""
   for letter in word:
      if letter.upper() not in vowel:
         result += letter
   return result

