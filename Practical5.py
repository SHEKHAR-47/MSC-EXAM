# Aim: Write a program to Implement syntactic parsing of a given text.

# Background Information:
# Syntactic Parsing: Syntactic parsing involves the analysis of words in the
# sentence for grammar and their arrangement in a manner that shows the
# relationships among the words.

Code:
import nltk
# nltk.download(&#39;punkt&#39;)
# nltk.download(&#39;averaged_perceptron_tagger&#39;)
# nltk.download(&#39;maxent_ne_chunker&#39;)
# nltk.download(&#39;words&#39;)
# nltk.download(&#39;treebank&#39;)
text = &quot;I ate hot ice-cream ,before match start&quot;
words = nltk.word_tokenize(text)
tagged_words = nltk.pos_tag(words)
syntactic_tree = nltk.ne_chunk(tagged_words, binary=True)
print(&quot;Syntactic tree:&quot;, syntactic_tree)

# Output:
# Syntactic tree: (S I/PRP ate/VBP hot/JJ ice-cream/NN ,/, before/IN match/JJ
# start/NN)

# Conclusion: Thus, we have successfully implemented syntactic parsing of a
# given text.
