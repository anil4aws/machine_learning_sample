# RANDOM VARIABLE

Random variables are values that depend on chance.  
They are denoted by `X` and `Y`.  
Examples of random variables include the outcome of a dice roll or the number of defective pieces in a batch.

---

## Discrete Random Variables

- Takes selected values within a certain range.

## Continuous Random Variables

- Takes any value within a certain range.

---

### Comparison between Discrete and Continuous Random Variables

| **Discrete Random Variables**                                    | **Continuous Random Variables**                         |
|------------------------------------------------------------------|--------------------------------------------------------|
| Takes selected values within a certain range.                    | Takes any value within a certain range.                |
| **Example:** Numbers on a dice.                                  | **Example:** Height of a person, weight, volume.       |

---

![Continuous Probability Distribution](https://github.com/anil4aws/machine_learning_sample/blob/main/images/continuous_pd.png)

---

## Discrete Probability Distribution

Based on Bernoulli trials and principles.

1. **Binomial Distribution**:  
2. **Poisson Distribution**: The number of opportunities for outcomes cannot have an upper limit.  
   - Example: Number of potential visitors in a store.
   - X is a random variable indicating the number of occurrences, with p(x) = 0, 1, 2, ... depending on the expected value λ (lambda).

### Poisson Distribution Parameters

- λ (lambda) is the parameter of the distribution.  
- When X follows a Poisson distribution with parameter λ (lambda):
  - **E(X)** = λ  
  - **Var(X)** = λ  
  - **s.d.(X)** = √λ

![Expected Value](https://github.com/anil4aws/machine_learning_sample/blob/main/images/Expected_Value.jpg)

---

### Binomial by Poisson Theorem

If `n` is very large and `p` is very small, then  
λ = n * p

---

### Poisson Probabilities

If `X` is the random variable representing the number of occurrences in a given interval, where the average rate of occurrence is λ, then:  
\[ P(X=r) = \frac{e^{-\lambda} (\lambda^r)}{r!} \]  
where r = 0, 1, 2, 3.

#### Example Problem:  
Find the probability of getting 3 or more defectives in a lot of 1000 when the probability of getting a defective is 0.005.  
- X = n = 1000 ; p = 0.005 (since n is very large and p is very small)  
- λ = n * p = 5

Thus,  
\[ Pr(X \geq 3) = 1 - Pr(X \geq 2) \]

Calculating the sum of Poisson probabilities:  
\[ Pr(X \geq 3) = (e^{-5}) \cdot \frac{5^0}{0!} + (e^{-5}) \cdot \frac{5^1}{1!} + (e^{-5}) \cdot \frac{5^2}{2!} \]

Result:  
\[ Pr(X \geq 3) = 0.87535 \]

---

## Continuous Probability Distribution

### Uniform Probability Distribution

If \( P(X) \) follows a uniform distribution in the range [a, b], the probability of lying in the range [c, d] is directly proportional to the length.  
\[ Pr(c < X < d) = \frac{d - c}{b - a} \]  
where \( a \leq c \leq d \leq b \).

---

### Normal Distribution

The curve is symmetric about the population mean \( \mu \).

![Normal Distribution](https://github.com/anil4aws/machine_learning_sample/blob/main/images/normal_Distribution.jpg)

---

![Normal Standard Distribution](https://github.com/anil4aws/machine_learning_sample/blob/main/images/Normal_Standard_Distribution.jpg)
