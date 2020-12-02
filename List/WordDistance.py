# function to calculate the minimum distance between w1 and w2 in s
   # get individual words in a list
   # assume total length of the string as minimum distance 
   # traverse through the entire string
   # the distance between the words is the index of the first word - the current word index
       # comparing current distance with the previously assumed distance 
def distance(s, w1, w2):  
    if w1 == w2 : 
        return 0   
    words = s.split(" ")    
    min_dist = len(words)+1 
    for index in range(len(words)): 
        if words[index] == w1: 
            for search in range(len(words)): 
                if words[search] == w2:  
                    curr = abs(index - search)-1
                    if curr < min_dist: 
                        min_dist = curr 

    # w1 and w2 are same and adjacent 
    return min_dist 
          
  
# Driver code 
s = "Amazon is the best company to work for. The amazon is a beautiful forest"
w1 = "Amazon"
w2 = "The"
print(distance(s, w1, w2)) 

'''# function to calculate the minimum  
# distance between w1 and w2 in s 
   
def distance(s, w1, w2):  
      
    if w1 == w2 : 
       return 0
  
    # get individual words in a list 
    words = s.split(" ") 
  
    # assume total length of the string as 
    # minimum distance 
    min_dist = len(words)+1 
  
    # traverse through the entire string 
    for index in range(len(words)): 
  
        if words[index] == w1: 
            for search in range(len(words)): 
  
                if words[search] == w2:  
  
                    # the distance between the words is 
                    # the index of the first word - the  
                    # current word index  
                    curr = abs(index - search) - 1
  
                    # comparing current distance with  
                    # the previously assumed distance 
                    if curr < min_dist: 
                       min_dist = curr 
  
    # w1 and w2 are same and adjacent 
    return min_dist 
      
  
# Driver code 
s = "Geeks for geeks practice contribute practice"
w1 = "Geeks"
w2 = "practice"
print(distance(s, w1, w2)) '''
