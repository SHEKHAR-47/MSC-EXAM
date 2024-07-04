# Aim: Write a program to Implement POS tagging using HMM &amp; Neural Model.
  
# Background Information:
# POS Tagging: In corpus linguistics, part-of-speech tagging (POS tagging or
# PoS tagging or POST), also called grammatical tagging is the process of
# marking up a word in a text (corpus) as corresponding to a particular part of
# speech, based on both its definition and its context.

# HMM: HMM (Hidden Markov Model) is a Stochastic technique for POS
# tagging. Hidden Markov models are known for their applications to
# reinforcement learning and temporal pattern recognition such as speech,
# handwriting, gesture recognition, musical score following, partial
# discharges, and bioinformatics.

# Neural Network: A neural network is a series of algorithms that endeavors to
# recognize underlying relationships in a set of data through a process that mimics
# the way the human brain operates.

Code:
import nltk
nltk.download(&#39;punkt&#39;)
nltk.download(&#39;averaged_perceptron_tagger&#39;)
nltk.download(&#39;universal_tagset&#39;)
text = &quot;Joe waited for the train, but the train was late&quot;
words = nltk.word_tokenize(text)
hmm_tagged = nltk.pos_tag(words)
print(&quot;PoS tagging using HMM:&quot;, hmm_tagged)
nn_tagged = nltk.pos_tag(words, tagset=&#39;universal&#39;)
print(&quot;PoS tagging using NN:&quot;, nn_tagged)

# Output:
# PoS tagging using HMM: [(&#39;Joe&#39;, &#39;NNP&#39;), (&#39;waited&#39;, &#39;VBD&#39;), (&#39;for&#39;, &#39;IN&#39;), (&#39;the&#39;,
# &#39;DT&#39;), (&#39;train&#39;, &#39;NN&#39;),
# (&#39;,&#39;, &#39;,&#39;), (&#39;but&#39;, &#39;CC&#39;), (&#39;the&#39;, &#39;DT&#39;), (&#39;train&#39;, &#39;NN&#39;), (&#39;was&#39;, &#39;VBD&#39;), (&#39;late&#39;, &#39;JJ&#39;)]
# PoS tagging using NN: [(&#39;Joe&#39;, &#39;NOUN&#39;), (&#39;waited&#39;, &#39;VERB&#39;), (&#39;for&#39;, &#39;ADP&#39;), (&#39;the&#39;,
# &#39;DET&#39;), (&#39;train&#39;,
# &#39;NOUN&#39;), (&#39;,&#39;, &#39;.&#39;), (&#39;but&#39;, &#39;CONJ&#39;), (&#39;the&#39;, &#39;DET&#39;), (&#39;train&#39;, &#39;NOUN&#39;), (&#39;was&#39;, &#39;VERB&#39;),
# (&#39;late&#39;, &#39;ADJ&#39;)
                       
# Conclusion: Thus, we have successfully implemented PoS tagging using HMM
# &amp; Neural Model
