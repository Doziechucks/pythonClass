
def vowel_check(done):
   numberOfString = 0
   for alphabet in done:
      if alphabet.lower() == "a" or alphabet.lower() == "e" or alphabet.lower() == "i" or alphabet.lower() == "o" or alphabet.lower() == "u":
         numberOfString = numberOfString + 1
   return numberOfString

