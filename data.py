x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) 

def wordcount():
    give_me_a_sentence = input("give me a sentence")
    word = give_me_a_sentence.split()
    print(word)
    

wordcount()