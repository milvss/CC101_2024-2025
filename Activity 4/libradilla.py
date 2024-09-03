sampleText2 = "my name is {0}. i love {1} and playing {2}"
sampleText2a = sampleText2. format("milva", "chicken", "billiards")
print(sampleText2a)


sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(name="mangs", food="sushi", play="COD")
print(sampleText3a)


item = "milk"
cost = 35.50
sampleText4 = "the product %s cost %.2f" %  (item, cost)
print(sampleText4)
