def searcher(constant, numbers):
   for number in range(len(numbers)):
      if constant == numbers[number]:
         return f"index {number}"
   return "not available"  
         

def searcher_two(numbers):
   negatives = 0
   zeros = 0
   positives = 0
   for number in range(len(numbers)):
      if numbers[number] < 0:
         negatives = negatives + 1
      if numbers[number] == 0:
         zeros = zeros + 1
      if numbers[number] > 0:
         positives = positives + 1
   return f"\nnegatives: {negatives} \nzeros: {zeros} \npositives: {positives}"
   
   