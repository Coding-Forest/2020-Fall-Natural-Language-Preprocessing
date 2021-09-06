### **Week 2 Mentoring session log** 

#### **Supervised learning**

- dataset must be labelled.

- Unsupervised learning

- Dimensionality reduction, clustering
- Dataset is unlabelled

#### Semi-supervised learning

- Hibrid learning
- Used when labellings is incomplete
- Uses mixture of labelled and unlabelled dataset.

#### Reinforcement learning

- Explores the reward
- Frequently used in games

##### **Loss function ** 

###### - Update weights through differentiation Word Embedding

#### **Word Embedding**

- Vectorise words; transform representations (str -> int)

  - One-hot encoding

  - **Word2Vec**
    - ```Word2Vec(datasets, vector_size= ?, workers=num_processes, sg=0(CBOW), window=(num_of_neighbours), min_count=(threshold to filter candidate words for embedding))```
  - CBOW (Continuous)
  - Skip-gram
  - FastText
  - SISG (Subword Information Skip Gram)
    - n-gram tokenisation

- **Problem with Word embedding**
  - Unknown words frequently appear.
  - Removing stop words.

- **Switch Transformer** (Google's latest publication in January, 2021 )



#### **Our week 2 task**

1. **Produce word embeddings**

2. **Word similiarity analysis**
   - Loop through the process until the analysis improves.
   - Source code is provided.
   - Wikipedia dump + mecab phoneme analysis
   - ```Gensim, Word2Vec```

- Pre-processing should be performed under consistent policy

- Additional libraries: ```Fasttext, GloVe, Swivel```

3. **Submit a report, which should include:**
   - Team discussion
     - Include all your n results.
     - Interprete the results. (why one result is better than the other?)
     - Explain the intention for your architectur design.
     - **Deadline: 9th Thursday 11am**



**Week 2 timeline**

- **Thursday 9th, 2pm Report** and feedback session
- **Friday 10th, 4pm Final report**