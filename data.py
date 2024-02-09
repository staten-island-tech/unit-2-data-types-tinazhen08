#Challenge: Ask user to input sentence, accept sentence, and tell user how many words are in the sentence
def wordcount():
    give_me_a_sentence = input("give me a sentence")
    word = give_me_a_sentence.split()
    print(len(word))
    
wordcount()