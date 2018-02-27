#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility
from nltk.tokenize import sent_tokenize
from pprint import pprint
import random
import time
import sys


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self:
            self[word] += count
        else:
            self.types +=1 
            self[word] = count
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self:
            print("{}: {}".format(word, self[word]))
            return self[word]
        else:
            return 0

    def unique_words(self):
        """ Return words that have a value of one """
        return [key for key, val in self.item() if val==1] 

    def export_histogram(self, histogram_title):
        """ Create a text file of histogram based on file name """
        file =  open(histogram_title+'.txt', 'w')
        for key, val in self.items():
            string = "{} {}\n".format(key,val)
            file.write(string)
        file.close()

def weighted_hist(dictogram):
    """Return a dictionary with value equal to value/tokens"""
    total = sum([val for val in dictogram.values()])
    weight_dict = {}
    for key,val in dictogram.items():
        weight_dict[key] = val/total
    return weight_dict

    def counts_dictionary(self):
        """ Returna a dictionary of counts and words """
        list_count= {}
        for key,val in self:
            print(val)

def time_diffrence(start_time):
    """ Returns the time diffrence between the start and time the function is called """ 
    return time.time()-start_time

def read_file(file_name):
    """ Read in text files based on file name """
    print('This should read the file {} in as text'.format(file_name))
    with open(file_name) as f:
        return f.read()


            

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('Weigted dictogram {}'.format(weighted_hist(histogram)))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))

def stochastic_sampling(weighted_hist):
    """Randomly choose a word in weighted histogram based on cumulative weights"""
    rand_percent = random.uniform(0,1)
    cum_weight = 0
    for key,token  in weighted_hist.items():
        cum_weight += token
        if cum_weight > rand_percent:
            return key
def main():
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

if __name__ == '__main__':
    main()
