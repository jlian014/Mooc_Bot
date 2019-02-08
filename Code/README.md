# EDA and Content Based Recommender

## 1. EDA

### Key findings from the EDA
- Categories of IT & Software, Personal_Development, Business, and Development have over 10000 courses. The IT & Software category has the most number of courses and the Photography category has the lease number of courses.
- 81.03% of the courses are taught in English. The third popular language is Portuguese. Other popular languages are including Spanish, Deutsch, Turkish, Japanese, French, Arabic, Russian and Chinese.
- Despite of many courses in IT and Software category, most of them are unrated. In contrast, the courses in the development courses are rated relatively high compare with other categories which have more than 10000 subscribers.
- Courses in the Development category has the most number of subscribers.
- Most courses are in a range from 0 to 25 hours, the courses in the Development category are  relatively long which is range from 0 to 50 hours. Surprisingly, there are some courses over 100 hrs.
- There's no clear linear relationship among course hours, number of subscribers and ratings.

Details are described in [HERE](./01_Data_Cleaning_and_EDA)


## 2. Convert texts into vectors
The text embedding converts text (words or sentences) into a numerical vector, they encode words and sentences in fixed-length dense vectorsto drastically improve the processing of textual data.

Universal Embeddings: embeddings that are pre-trained on a large corpus and can be plugged in a variety of downstream task models to automatically improve their performance by incorporating some general word/sentence representations learned on the larger dataset.

Google’s Universal Sentence Encoder, published in early 2018. Their encoder uses a transformer-network that is trained on a variety of data sources and a variety of tasks with the aim of dynamically accommodating a wide variety of natural language understanding tasks. The pre-trained Universal Sentence Encoder is publicly available in Tensorflow-hub.. The model is efficient and result in accurate performance on diverse transfer tasks.

![https://www.tensorflow.org/hub/modules/google/universal-sentence-encoder/1](https://cdn-images-1.medium.com/max/1600/1*qACWEt8866AOKEYRb-Y5ig.png)

At first, we have generated a `BASE_VECTORS` by applying Universal Encoder to the `objective_summray` of the course. Then, we have created a function that convert the input text as a 512 x 1 vector, and use cosine similarity to find simiarity between two vectors (the input text vector and `BASE_VECTORS`. This is nothing but finding the cosine of angle between two vectors. The formula is direcly taken from dot prduct of vectors:

$$
cos(\theta) = \frac{A \cdot B}{\left\| A\right\| \left\| B\right\| } = \frac{A \cdot B}{\sqrt{\sum{A_i^2}} \cdot \sqrt{\sum{B_i^2}}}
$$

The function will find the most similar `objective_summary` with the search term and return 5 top closet courses matches to the search term and has higher number of subscribers and ratings.

The details are described in [HERE](./02_Content_Based_Recommender).
