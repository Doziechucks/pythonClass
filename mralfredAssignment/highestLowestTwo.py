def find_highest_and_lowest():
   nameList = []
   pythonScoreList = []
   javaScoreList = []
   dataScienceScoreList = []
   designThinkingScoreList = []
   position1 = 0
   position2 = 0
   position3 = 0
   position4 = 0
   position5 = 0
   position6 = 0
   position7 = 0
   position8 = 0
   for number in range(2):
      name = input("Enter name: ")
      nameList.append(name)
      for subjects in range(1):
         pythonScore = int(input("Enter python score: "))
         pythonScoreList.append(pythonScore)

         javaScore = int(input("Enter java score: "))
         javaScoreList.append(javaScore)

         dataScore = int(input("Enter Data science score: "))
         dataScienceScoreList.append(dataScore)

         designThinking = int(input("Enter Design thinking score: "))
         designThinkingScoreList.append(javaScore)

   
   highestPython = pythonScoreList[0]
   lowestPython = pythonScoreList[0]
   for frequency in range(0, len(pythonScoreList)):
      if pythonScoreList[frequency] > highestPython:
         highestPython = pythonScoreList[frequency]
         position1 = pythonScoreList.index(highestPython) 
   print(f"{nameList[position1]} scored highest in python")

   for frequency in range(0, len(pythonScoreList)):
      if pythonScoreList[frequency] < lowestPython:
         lowestPython = pythonScoreList[frequency]
         position2 = pythonScoreList.index(lowestPython)
   print(f"{nameList[position2]} scored lowest in python")

   highestjava = javaScoreList[0]
   lowestjava = javaScoreList[0]
   for frequency in range(0, len(javaScoreList)):
      if javaScoreList[frequency] > highestjava:
         highestjava = javaScoreList[frequency]
         position3 = javaScoreList.index(highestjava)
   print(f"{nameList[position3]} scored highest in java")

   for frequency in range(0, len(javaScoreList)):
      if javaScoreList[frequency] < lowestjava:
         lowestjava = javaScoreList[frequency]
         position4 = javaScoreList.index(lowestjava)
   print(f"{nameList[position4]} scored lowest in java")


   highestDataScience = dataScienceScoreList[0]
   lowestDataScience = dataScienceScoreList[0]
   for frequency in range(0, len(pythonScoreList)):
      if dataScienceScoreList[frequency] > highestDataScience:
         highestDataScience = dataScienceScoreList[frequency]
         position5 = dataScienceScoreList.index(highestDataScience)
   print(f"{nameList[position5]} scored highest in DataScience")

   for frequency in range(0, len(pythonScoreList)):
      if dataScienceScoreList[frequency] < lowestDataScience:
         lowestDataScience = dataScienceScoreList[frequency]
         position6 = dataScienceScoreList.index(lowestDataScience)
   print(f"{nameList[position6]} scored lowest in DataScience")


   highestDesignThinking = designThinkingScoreList[0]
   lowestDesignThinking = designThinkingScoreList[0]
   for frequency in range(0, len(designThinkingScoreList)):
      if designThinkingScoreList[frequency] > highestDesignThinking:
         highestDesignThinking = designThinkingScoreList[frequency]
         position7 = designThinkingScoreList.index(highestDesignThinking)
   print(f"{nameList[position7]} scored highest in DesignThinking")

   for frequency in range(0, len(designThinkingScoreList)):
      if designThinkingScoreList[frequency] < lowestDesignThinking:
         lowestDesignThinking = designThinkingScoreList[frequency]
         position8 = designThinkingScoreList.index(lowestDesignThinking)
   print(f"{nameList[position8]} scored lowest in DesignThinking")

find_highest_and_lowest()
