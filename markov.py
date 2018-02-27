from __future__ import division, print_function  # Python 2 and 3 compatibility
from nltk.tokenize import sent_tokenize
from dictogram import *
import numpy

class Markov(dict):
    """Markov is a dictionary of key(current word), val/next_word(dictogram). Takes a string of text"""
    def __init__(self, text=None,order=2):
        #Create start and stop dictogram to store the begging of words and end of words
        self['START'] = Dictogram()
        self.order = order
        if text:
            #Creating a markov model for each sentence
            self.markov(text)

    def tokenize_sentence(self, text):
        """ Using nltk split corpus based on sentences"""
        sentence_arr = sent_tokenize(text)
        print("There are {} sentences".format(len(sentence_arr)))
        return sentence_arr


    def markov(self,text,):
        """ Create a markoff model based on the text array input into the file """
        corpus = self.tokenize_sentence(text)
        x = 0
        for sentence in corpus: #For every sentence Add START STOP to create seperate chain
            sentence = sentence.split()
            x = 0
            self['START'].add_count(tuple(sentence[0:self.order]))
            # From the first to the to last word
            while x< len(sentence)-self.order:
                word = tuple(sentence[x:x+self.order])
                next_word = tuple(sentence[x+1:self.order+x+1])
                # print('{} | {}'.format(word,next_word))
                if word not in self.keys():
                    self[word]= Dictogram()
                self[word].add_count(next_word)
                x+=1
            # Adding a stop token to the final word
            last_word= tuple(sentence[-self.order:])
            self[last_word] = Dictogram()
            self[last_word].add_count('STOP')

    def weight_markov(self):
        """ Return a key with a value of possible next words weighte """
        markov_weight = {}
        for key, val in self.items():
            markov_weight[key] = weighted_hist(val)
        return markov_weight

    def generate_sentence(self, length=10):
        """Return a sentence based on markov model"""
        sentence = ""
        weights = self.weight_markov()
        # print(self.text)
        # print(weights)
        #Get First word
        word = stochastic_sampling(weights['START'])
        sentence += " ".join(word)
        words = 1
        while words <= length:
            word = stochastic_sampling(weights[word])
            if word == 'STOP':
                break
            sentence +=" "+" ".join(word[self.order-1:])
        print(sentence)
        return sentence
def main():
        marky = Markov(read_file('neil.txt'),2)
        weighted_markov = marky.weight_markov()
        marky.generate_sentence()
if __name__ == '__main__':
    main()
#if self.order changes generate a new markov chain with new self.order
# else generate sentces based on old chains
