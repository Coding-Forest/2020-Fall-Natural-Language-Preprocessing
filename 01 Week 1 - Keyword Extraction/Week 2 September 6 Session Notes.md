## Week 2 September 6 Monday Session Notes 

- Supervised learning 
  - Dataset must be labelled
- Unsupervised learning
  - Dimensionality reduction, clustering
  - Dataset is unlabelled

- **Semi-supervised learning**
  - Hibrid learning
  - Used when labellings is incomplete
  - Uses mixture of labelled and unlabelled dataset.

- **Reinforcement learning**
  - Explores the ***reward***
  - Frequently used in games

### **Loss function**

Update weights through differentiation

### **Word Embedding**

- Vectorise words (turn strings into numbers)
- One-hot encoding
- Transform representation (str -> int)

## **Word2Vec**

**Algorithms**

- ```CBOW``` Continuous Bag Of Words
- ```Skip-gram```
- ```FastText```
- ```SISG``` Sub-word Information Skip Gram
- n-gram tokenisation

**Problems with word embedding**

- Unknown words appear frequently.
- Removing stop words.

- Switch Transformer (Google's latest publication in January, 2021 )



---



## **Week 2 task**

- Source code is provided.
  - Wikipedia dump + mecab phoneme analysis
  - ```Gensim Word2Vec```

1) Pre-processing should be consistent
   - ```Fasttext```, ```GloVe```, ```Swivel```

2. Produce word embeddings
3. Word similiarity analysis
   - Loop through the process until the analysis improves.
4. Report
   - Explain the intention for your architecture design.
   - Include all your n results.
   - Interpret the results. (why a specific result is better than the rest?)

**Timeline**

- Deadline: 9th Thursday 11am
- Thursday 9th, 2pm Report and feedback session
- Friday 10th, 4pm Final report.



**Challenges**

- ```Word2Vec(datasets, vector_size= ?, workers=num_processes, sg=0(CBOW), window=(num_of_neighbours), min_count=(threshold to filter candidate words for embedding))```

- Solve the problem of words not present in the word embedding
  - Figure out:
    - The reason why they are not included, and
    - how you can include them

- Additional task: visualise your work!
