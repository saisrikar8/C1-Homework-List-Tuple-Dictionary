'''
3/4/2021

Review

List Functions
1. Addition
  LIST.append(ELEMENT)    #Adds element/item at the end of the list
  LIST.insert(INDEX, ELEMENT)     #Insert element at the give index

2. Removing
  LIST.remove(ELEMENT)      #Search the element/item and remove
  LIST.pop(INDEX)          #Removes the element at the given index
  #Ex.

 3. Replacing
numbers = [1,3,3,4] # I want to have 1, 2, 3, 4
numbers[1] = 2
print (numbers) # New List: [1,2,3,4]

# Ex.

number = [1,4,6,5,7,2]

# 1. Add 2 and 3 between 1 and 4
number.insert(1,2)
number.insert(2,3)

# 2. Add 5 between 4 and 6
number.insert(4, 5)

# 3. Remove 5 between 6 and 7
number.pop(6)

# 4. Remove 2 at the end
number.pop(7)

# 5. Add 8, 9, 10 at the end
number.insert(7,8)
number.append(9)
number.append(10)
print (number)


3. Replacing

numbers = [1,3,3,4].     #I want to have 1,2,3,4
numbers[1] = 2
print(numbers). #New list [1,2,3,4]



==============================================

Tuple
Another type of list, stores data/values inside parenthesis, (). Unlike a list, it cannot be changed(immutable). It still uses an index like a list.

color = ("Blue", "Red", "Black", "Green", "Yellow", "White")
print(color[3])



'''
