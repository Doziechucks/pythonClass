
def word_anagram(word, anagram):

   catch = 0
   if len(word) != len(anagram):
      return False
   else:   
      for letter in range(len(word)):
         for alphabet in range(len(anagram)):
            if word[letter] == anagram[alphabet]:
               catch += 1            
      if catch == len(word):
         return True
      else:
         return False

  