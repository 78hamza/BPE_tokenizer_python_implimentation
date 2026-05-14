from typing import *
from collections import defaultdict, Counter
import collections
import re


class BPE:
    def __ini__(self):
        pass

    """Start with a dictionary of words -> frequencies, we append `_` to each word to mark end of word"""
    def get_vocab(self):
        pass

    """the vocabulary words are stored as strings with spaces betwee each symbol, we count each adjacent pair of symbols"""
    def count_pairs(self):
        pass


    """
    Given the most frequent words pair (e.g,. ('e', 's')), we replace occurences in ll words using a regex, 
    for clarity we printed the updaed vocab each time
    """
    def merge_pair(self):
        pass


    """
    train_bpe: Iteratively perfoms merges, printing each step. we stop after a fixed number of merges (num_merges).
    The filan vocabulary maps merged tokens (characters merged without spaces) to frequencies.
    """
    def train_bpe(self):
        pass

    """
    encode_pbe: To tokenize a new wordk we split it inot characters plus "_", then applythe merge rules in order (finding
    and merging adjacent tokens). Any leftover symbol not in vocab would become [UNK] (we cold add that logic)
    """
    def encode_pbe(self):
        pass

    """
    decode_bpe: joins tokens and remove underscore to recover the original word
    """
    def decode_bpe(self):
        pass
