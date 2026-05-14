from typing import *
from collections import defaultdict, Counter
import re


class BPE:
    def __init__(self, corpus: dict) -> None:
        self.corpus: list = corpus
        self.vocab: dict = Counter()


    """Start with a dictionary of words -> frequencies, we append `_` to each word to mark end of word"""
    def get_vocab(self):
        """Build base vocabulary: count word frequencies (with end-of-word '_')"""
        for word in self.corpus:
            self.vocab[word + '_'] += 1
        return self.vocab

    """the vocabulary words are stored as strings with spaces betwee each symbol, we count each adjacent pair of symbols"""
    def count_pairs(self) -> dict:
        pairs = Counter()
        for word, freq in self.vocab.items():
            symbols = word.split(" ")
            # Note our vocab words currently have spaces between each character
            for i in range(len(symbols) - 1):
                pair = (symbols[i], symbols[i+1])
                pairs[pair] += freq
        return pairs

    """
    Given the most frequent words pair (e.g,. ('e', 's')), we replace occurences in ll words using a regex, 
    for clarity we printed the updaed vocab each time
    """
    def merge_pair(self, pair) -> dict:
        """mergethe given pair in all vocab words."""
        bigram = ' '.join(pair)
        replacement = ''.join(pair) # the new merged symbol
        new_vocab = {}
        for word, freq in self.vocab.items():
            # replace all occurences of the pair
            new_word = re.sub(r'\b{}\b'.format(bigram), replacement, word)
            new_vocab[new_word] = freq
        return new_vocab


    """
    train_bpe: Iteratively perfoms merges, printing each step. we stop after a fixed number of merges (num_merges).
    The filan vocabulary maps merged tokens (characters merged without spaces) to frequencies.
    """
    def train_bpe(self, num_merges: int) -> tuple:
        for word, freq in self.corpus.items():
            spaced = ' '.join(list(word)) + ' _'
            self.vocab[spaced] = freq

        merges = []
        for i in range(num_merges):
            pairs = self.count_pairs()
            if not pairs:
                break
            # find most frequent pair
            best_pair, best_freq = max(pairs.items(), key=lambda x: x[1])
            merges.append(best_pair)
            # merge in vocab
            self.vocab = self.merge_pair(best_pair)
            print(f"Merge {i+1}: {best_pair} (count={best_freq})")
            for w, f in self.vocab.items():
                print(f" {w}: {f}")
            print()
        # build the final merged vocab
        final_vocab = {}
        for word, freq in self.vocab.items():
            token = word.replace(' ', '')
            final_vocab[token] = freq
        return merges, final_vocab
            
            

    """
    encode_pbe: To tokenize a new wordk we split it inot characters plus "_", then applythe merge rules in order (finding
    and merging adjacent tokens). Any leftover symbol not in vocab would become [UNK] (we cold add that logic)
    """
    def encode_pbe(self, word: str, merges: list) -> list:
        """
        encode a single word (string) using learned merge rules.
        returns list of tokens , Unkonw (unmerged) chars become <UNK>
        """
        # initialize as a list of characters + '_'
        symboles = list(word) + ['_']
        tokens = symboles.copy()
        for a, b in merges:
            pair = a + b
            i = 0
            while i < len(tokens)-1:
                if tokens[i] == a and tokens[i+1] == b:
                    # merge the pair
                    tokens[i] = pair
                    del tokens[i+1]
                else:
                    i += 1
        # replace any symbol not in final vocab with [UNK]
        # Assumes merges covers tem; here we skip check
        return tokens

    """
    decode_bpe: joins tokens and remove underscore to recover the original word
    """
    def decode_bpe(self, tokens):
        """Detokenize by joining tokens and removing underscore markers"""
        text = ''.join(tokens).replace('_', '')
        return text
