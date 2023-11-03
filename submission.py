import collections
import math
from math import sqrt
from typing import Any, DefaultDict, List, Set, Tuple
from itertools import permutations
from collections import defaultdict


############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in
the sparse vector, while the values represent the elements at those positions.
Any key which is absent from the dict means that that element in the sparse
vector is absent (is zero).
Note that the type of the key used should not affect the algorithm. You can
imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors,
but it should work the same way with arbitrary keys (e.g., "red", "blue", 
"green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 4a

def find_alphabetically_first_word(text: str) -> str:
    """
    Given a string |text|, return the word in |text| that comes first
    lexicographically (i.e., the word that would come first after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() handy here. If the input text is an empty string, 
    it is acceptable to either return an empty string or throw an error.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")  
    w = text.split()  # Divide a string em palavras
    if not w:  # Verifique se a lista de palavras está vazia
        raise ValueError("String vazia irmao")
    p_palavra = min(w, key=str)# apanhaa a palavra minima  
    u_palavra = max(w, key=str)# apanha a maxima

    print(p_palavra +" -- "+  u_palavra)
    return p_palavra +u_palavra
    # END_YOUR_CODE

############################################################
# Problem 4b


def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    
    locX1 = loc1[0]
    locY1 = loc1[1]
    locX2 = loc2[0]
    locY2 = loc2[1]
    distancia = sqrt((locX1 - locX2)**2 + (locY1 - locY2)**2) #formula geral para calcular a distancia euclideana
    print(distancia)
    return distancia

    # END_YOUR_CODE\

############################################################
# Problem 4c

def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")

    num_words = len(sentence)
    similar_sentences = set()
    for perm in permutations(sentence):
        new_sentence = " ".join(perm) 

        if len(perm) == num_words and all(sentence[i] + " " + sentence[i+1] in sentence for i in range(num_words - 1)):
            similar_sentences.add(new_sentence)

    return list(similar_sentences)
    # END_YOUR_CODE


############################################################
# Problem 4d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros)
    |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    
    dot_product = 0.0

    
    for key in v1:
        if key in v2:
            dot_product += v1[key] * v2[key]

    return dot_product

# Exemplo de uso
v1 = defaultdict(float, {'a': 1.0, 'b': 2.0, 'c': 0.0, 'd': 3.0})
v2 = defaultdict(float, {'a': 2.0, 'b': 1.0, 'c': 0.0, 'd': 0.0})
result = sparse_vector_dot_product(v1, v2)
print(result)

    # END_YOUR_CODE

############################################################
# Problem 4e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector,
) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    for key, value in v2.items():
        v1[key] += scale * value

    # END_YOUR_CODE


############################################################
# Problem 4f

def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of words that
    occur more than once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    
    word_count = defaultdict(int)
    words = text.split()

    # Contagem de palavras
    for word in words:
        word_count[word] += 1

    # Retorne um conjunto de palavras que repetem mais do q uma vez
    nonsingleton_words = {word for word, count in word_count.items() if count > 1}

    return nonsingleton_words

# Exemplo de uso
text = "o gato gato preto é um gato preto"
result = find_nonsingleton_words(text)
print(result)

    # END_YOUR_CODE



find_alphabetically_first_word("banana maca abacaxi")
euclidean_distance([1,2],[2,3])
