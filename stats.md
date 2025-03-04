#  Descriptive stats
----------------------------------
## Measures of central tendencies 

Central tendency : A single numerical value around which data tends to cluster , used to give summary measure 
factory output will giv

[![measureofcentraltendency](https://github.com/anil4aws/machine_learning_sample/blob/main/images/measureofcentraltendency.jpg)

### Mathematical and positional averages 
-------------------------------------


#### 1. Mathematical average : sum of all values / no of values : also known as mean . 
*** If data is evenly distributed *****

#### 2. positional average

Common measures of central tendency 

#### Arthimetic mean : Mean , Geometric mean , Harmonic mean, Median and Mode 

#### Median : central value ,giving q1(25%) and q2 (median ) and q3(75%)

[![median](https://github.com/anil4aws/machine_learning_sample/blob/main/images/median.jpg)

#### Quartile 
[![iqr](https://github.com/anil4aws/machine_learning_sample/blob/main/images/iqr.jpg)


#### Decile - 9 values dividing data into 10 parts

#### Mode : Is most frequent occuring obersrvation 

[![mode](https://github.com/anil4aws/machine_learning_sample/blob/main/images/mode.jpg)

#### Empirical relationship of mean, median and mode :
(Mean - Mode) = 3 *(Mean - Median)



#### Measures of Diseprsion : Is and index that quantifies degree to which data is dispersed or spread

Ex : 

     player 1 : 5  , 15 , 15 ,  25

     player 2 : 10 , 15 , 15 ,  20

1. range of : range between max and min , impacted by extreme values . valuable if outliers ae removed 

2. quartile deviation : is half the difference between q1 and q3 - not impacted by extreme values

3. Mean absolute deviation : above arithimetic mean above is 15. 
values of deviation from mean is

 -10 , 0 , 0 , 10  = sum of deviation is 0 alwyas so we use average of absolute deviation
   
  -5 , 0 , 0 ,5

Now mean deviation = (1/n)* Σ(x-x̄)

Now mean deviation will be 
Ex : 

     player 1 : 5  , 15 , 15 ,  25   = mean deviation = 5

     player 2 : 10 , 15 , 15 ,  20	 = mean deviation = 2.5

4. Standard deviation : measure of spread of the data 
Std deviation = √ (average of squares of deviation)

[![sd](https://github.com/anil4aws/machine_learning_sample/blob/main/images/sd.jpg)

5. variance : square of standard deviation  : how far a set of data is dispersed from mean or average value 
The symbol for variance is σ2, which is read as "sigma squared

σ2 =  [ (i=1-N)Σ(xi-μ)^2 ] / 2

σ2 - population variance 
Σ  - sum total 
N - Number of obersvations 
xi - ith obeservation in the population 
μ - population mean 

Ex : player 1 : 5  , 15 , 15 ,  25   = mean deviation = 5    = variance  = 50   = Standard deviation = 7.07
     player 2 : 10 , 15 , 15 ,  20	 = mean deviation = 2.5  = variance  = 12.5 = Standard deviation = 3.53

Like mean deviation standard deviation magnifies larger deviation  


#### Z score also known as standard score 

Number of deviations above or below arithmetic mean 
Data Set = [X1 , X2 .. Xi .. Xn]
Zj = (Xj-x̄)/s
s- standard deviation 

#### Empirical Rule

in bell curve which are symmetric , empirical rule says about  65% scores are between -1 to 1 
about  95% scores are between -2 to 2
99.7 between -3 and 3 . beyond that is outlier 

## co-efficient of variation 
To compare two data set for Dispersion in consumption = Standard deviation/Arithmetic Mean 
co-efficient of variation can also be used as measure of consistency : if scores are two individuals are same then individual with lower covariance is consistent 



## measures of shape 
--------------------

In normal distribution - skewness is 0 
for symmetrical mean , median and mode is identical 
If positively skewed - long tail towards right 
[![measuresofshape](https://github.com/anil4aws/machine_learning_sample/blob/main/images/measuresofshape.jpg)
[![kurtosis](https://github.com/anil4aws/machine_learning_sample/blob/main/images/kurtosis.jpg)


# measure of central tendency together with measure of dispersion and measure of skewness gives good summary of data



