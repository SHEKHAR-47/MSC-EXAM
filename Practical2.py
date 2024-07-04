# Aim: Write a program to Implement stemming and lemmatization.

# Background Information:
# Stemming: Stemming is the process of reducing a word to its stem that affixes
# to suffixes and prefixes or to the roots of words known as &quot;lemmas&quot;

# Lemmatization: Lemmatization is a text pre-processing technique used in
# natural language processing (NLP) models to break a word down to its root
# meaning to identify similarities. For example, a lemmatization algorithm would
# reduce the word better to its root word, or lemme, good.

# CODE
import nltk
# nltk.download(&#39;punkt&#39;)
# nltk.download(&#39;wordnet&#39;)
words = [&#39;eating&#39;, &#39;eats&#39;, &#39;eaten&#39;, &#39;eat&#39;]
stemmer = nltk.stem.PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print(&quot;Stemmed words:&quot;, stemmed_words)
lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(&quot;Lemmatized words:&quot;, lemmatized_words)

# Output:
# Stemmed words: [&#39;eat&#39;, &#39;eat&#39;, &#39;eaten&#39;, &#39;eat&#39;]
# Lemmatized words: [&#39;eating&#39;, &#39;eats&#39;, &#39;eaten&#39;, &#39;eat&#39;]

# Conclusion: Thus, we have successfully implemented stemming andlemmatization.
