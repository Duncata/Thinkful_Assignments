#!/usr/bin/env python
# coding: utf-8

# In[29]:


#print walking directory
pwd


# ### Drill - Describing Data

# 1. Greg was 14, Marcia was 12, Peter was 11, Jan was 10, Bobby was 8, and Cindy was 6 when they started playing the Brady kids on The Brady Bunch. Cousin Oliver was 8 years old when he joined the show. What are the mean, median, and mode of the kids' ages when they first appeared on the show? What are the variance, standard deviation, and standard error?
# 
# 2. Using these estimates, if you had to choose only one estimate of central tendency and one estimate of variance to describe the data, which would you pick and why?
# 
# 3. Next, Cindy has a birthday. Update your estimates- what changed, and what didn't?
# 
# 4. Nobody likes Cousin Oliver. Maybe the network should have used an even younger actor. Replace Cousin Oliver with 1-year-old Jessica, then recalculate again. Does this change your choice of central tendency or variance estimation methods?
# 
# 5. On the 50th anniversary of The Brady Bunch, four different magazines asked their readers whether they were fans of the show. The answers were: TV Guide 20% fans Entertainment Weekly 23% fans Pop Culture Today 17% fans SciPhi Phanatic 5% fans
# 
# 6. Based on these numbers, what percentage of adult Americans would you estimate were Brady Bunch fans on the 50th anniversary of the show?

# In[25]:


# 1 
import numpy as np
ages =[14,12,11,10,8,6,8]

def statistic(ages):
    print("mean of age: ",np.mean(ages))
    print("median of age: ",np.median(ages))
    print("variance of age: ",np.var(ages))
    print("std. deviation of age: ",np.std(ages))
    print("standard error of age: ",np.std(ages)/np.sqrt(len(ages)-1))
    
statistic(ages)
print("Mode is ages: 8")


# In[ ]:


# 2
#We can choose mean or standard deviation as mean and median are close in value.


# In[26]:


#3
ages2 =[14,12,11,10,8,7,1]
statistic(ages3)
print("There is no mode")
  
statistic(ages2)
print("Mode is 8")

# median & mode didn't change. 
# mean, variance, standard deviation, and standard error change a little.  


# In[27]:


# 4
ages3 =[14,12,11,10,8,7,1]
statistic(ages3)
print("There is no mode")

#use median, mean diverge due to outlier 1


# In[ ]:


# Question no. 5&6
# (.20+.23+.17)/3 = .20 0r 20% approximately
# SciPhi Fanatic is a special interest magazine for scifi
# whereas the others are more general and representa better sample
# so we average those three


# ## Basic Probability Drill Exercise

# #### See Statistic statistic handbook (NIST “Engineering Statistics Handbook” https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm)

# Now it’s time to compute some probabilities. Keep track of your work in a Google document or markdown file that you can share with your mentor.
# 
# 1. Calculate the probability of flipping a balanced coin four times and getting each pattern: HTTH, HHHH and TTHH.
# 
# 2.If a list of people has 24 women and 21 men, then the probability of choosing a man from the list is 21/45. What is the probability of not choosing a man?
# 
# 3.The probability that Bernice will travel by plane sometime in the next year is 10%. The probability of a plane crash at any time is .005%. What is the probability that Bernice will be in a plane crash sometime in the next year?
# 
# 4.A data scientist wants to study the behavior of users on the company website. Each time a user clicks on a link on the website, there is a 5% chance that the user will be asked to complete a short survey about their behavior on the website. The data scientist uses the survey data to conclude that, on average, users spend 15 minutes surfing the company website before moving on to other things. What is wrong with this conclusion?
# Discuss your answer to each of these questions with your mentor.

# 1. Calculate the probability of flipping a balanced coin four times and getting each pattern: HTTH, HHHH and TTHH.

# The answer to a, b, and c is the same: .5*.5*.5*.5=.0625 , because the patterns are ordered

# 2.If a list of people has 24 women and 21 men, then the probability of choosing a man from the list is 21/45. What is the probability of not choosing a man?
# 
# 24/45
# 

# 3.The probability that Bernice will travel by plane sometime in the next year is 10%. The probability of a plane crash at any time is .005%. What is the probability that Bernice will be in a plane crash sometime in the next year?
# 
# P=0.10 * 0.005= .0005

# 4.A data scientist wants to study the behavior of users on the company website. Each time a user clicks on a link on the website, there is a 5% chance that the user will be asked to complete a short survey about their behavior on the website. The data scientist uses the survey data to conclude that, on average, users spend 15 minutes surfing the company website before moving on to other things. What is wrong with this conclusion?
# 
# -People who surf longer are likely to click more links, increasing the odds of getting a survey

# In[ ]:


P(A | B) = P(B | A) * P(A) / P(B)

OR

P(A | B) = P(B | A) * P(A) / [P(A)*P(B|A) + P(A~)*P(B|A~)]


# In[28]:


#P(Infected| Positive Test) = P(Positive Test| Infected) * P(Infected) / P(Positive Test)

= .9999 * .000001/(.000001*.9999 + .999999*.0001) = .0099 or .99%


# ### Drill exercises on Bayes' Rule 

# A diagnostic test has a 98% probability of giving a positive result when applied to a person suffering from Thripshaw's Disease, and 10% probability of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person whose disease status is unknown. Calculate the probability that the test will:
# 
#     Be positive
#     Correctly diagnose a sufferer of Thripshaw's
#     Correctly identify a non-sufferer of Thripshaw's
#     Misclassify the person

# In[ ]:


Be positive= .98*.005 + .1*.995 = .1044
Correctly diagnose a sufferer of Thripshaw’s= .98
Correctly identify a non-sufferer of Thripshaw’s = .9
Misclassify the person= 1-(.98*.005 + .9*.995)=.0996


# ### Evaluating Data Sources

# In each of the scenarios, find possible shortcomings of the theoretical or actual data sources to answer the given question. What could be done to either adjust the analysis or reframe the question so that you can answer it accurately?
# 
# Data Source: Amsterdam availability data scraped from AirBnB on December 24th. Question: What are the popular neighborhoods in Amsterdam?
# 
# Data Source: Mental health services use on September 12, 2001 in San Francisco, CA and New York City, NY. Question: How do patterns of mental health service use vary between cities?
# 
# Data Source: Armenian Pub Survey. Question: What are the most common reasons Armenians visit local pubs?
# 
# Write up your answers and submit a link below.

# Amsterdam availability data scraped from AirBnB on December 24th:
# 
# Christmastime will bias availability in two ways- more AirBnBs may be taken due to vacationers, or fewer AirBnBs may be on offer because people don’t want to share their homes over the holidays. Choose a sampling period that doesn’t include a major holiday, or reframe the question to focus on popular neighborhoods during major holidays.
# 
# *Mental health services use on September 12, 2001 in San Francisco, CA and New York City, NY: Given the terrorist attack on NYC the day before, patterns of mental health services use are likely to be very different in the two cities-- even if they were pretty similar on September 10, 2001. Reframe the question to mental health use in the aftermath of a nearby vs distant crisis, perhaps.
# 
# *Armenian Pub Survey: Respondents are all university students. Reframe to ‘university students’ reasons to visit pubs.’

# ### Beware of Monty Hall problem

# Most people come to the conclusion that switching does not matter because there are two unopened doors and one car and that it is a 50/50 choice. This would be true if the host opens a door randomly, but that is not the case; the door opened depends on the player's initial choice, so the assumption of independence does not hold. Before the host opens a door there is a 
# 1
# /
# 3
#  probability the car is behind each door. If the car is behind door 1 the host can open either door 2 or door 3, so the probability the car is behind door 1 AND the host opens door 3 is 
# 1
# /
# 3
#  * 
# 1
# /
# 2
#  = 
# 1
# /
# 6
# . If the car is behind door 2 (and the player has picked door 1) the host must open door 3, so the probability the car is behind door 2 AND the host opens door 3 is 
# 1
# /
# 3
#  * 1 = 
# 1
# /
# 3
# . These are the only cases where the host opens door 3, so if the player has picked door 1 and the host opens door 3 the car is twice as likely to be behind door 2. The key is that if the car is behind door 2 the host must open door 3, but if the car is behind door 1 the host can open either door.

# ### The Normal Distribution and the Central Limit Theorem
# 

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


# Making a standard normally distributed variable with 1000 observations, a mean of 0, and 
# a standard deviation of 1, and putting it in a data frame.

mean = 0
sd = 1
n = 1000

df = pd.DataFrame({'rand': np.random.normal(mean, sd, 1000)})

# Plotting the variables in the data frame (here, just the variable "rand") as a histogram.
df.hist()

# Inline printing the histogram
plt.show()


# #### Let’s try a QQ plot to check if data is normally distributed:

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


# Making two variables.

rand1 = np.random.normal(50, 300, 1000)
rand2 = np.random.poisson(1, 1000)

# Sorting the values in ascending order.

rand1.sort()
rand2.sort()

# Making a standard normally distributed variable with 1000 observations,
# a mean of 0, and standard deviation of 1 that we will use as our “comparison.”

norm = np.random.normal(0, 1, 1000)

# Sorting the values in ascending order.

norm.sort()


# In[9]:


# Plotting the variable rand1 against norm in qqplots.

plt.plot(norm, rand1, 'o')
plt.show()


# In[10]:


# Plotting the variable rand2 against norm in qqplots.

plt.plot(norm, rand2, 'x')
plt.show


# ##### When data are not normal, the mean and standard deviation are no longer accurate or informative summaries. Let's make histograms of rand1 and rand2, then compute descriptive statistics to see how well they match up.

# In[72]:


#Plot a histogram for rand1.
plt.hist(rand1, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(rand1.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(rand1.mean()+rand1.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(rand1.mean()-rand1.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()




# In[73]:


print(rand1.mean())
print(rand1.std())


# In[13]:


# Plot the same histogram for rand2.

plt.hist(rand2, bins=20, color = 'c')

# Add a vertical line at the mean.

plt.axvline(rand2.mean(), color = 'b', linestyle= 'solid', linewidth= 2)

# Add a vertical line at one standard deviation above the mean.

plt.axvline(rand2.mean() + rand2.std(), color= 'b', linestyle= 'dashed', linewidth= 2)

#Add a vertical line at one standard deviation below the mean.

plt.axvline(rand2.mean() - rand2.std(), color= 'b', linestyle= 'dashed', linewidth= 2)

# Print the histogram.

plt.show()


# Because rand1 is normal, the mean is placed where the data clusters, with approximately 50% of the data falling on either side, and approximately 67% of the data falling within one standard deviation of the mean. For rand2, the mean is still placed where the data clusters, but the cluster is not centered, and the standard deviation does not encompass the same amount of data on each side of the mean. Put another way, for rand2 the mean is no longer a measure of "central" tendency, as it does not fall in the center, and the standard deviation no longer describes how much variance there is. Asymmetric probability distributions are described as "skewed."

# ##### Other Distribution

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


#Generate a bernoulli distribution with p = 0.5
bernoulli = np.random.binomial(1, 0.5, 1000)

#Plot a histogram.
plt.hist(bernoulli)

#Print the histogram
plt.show()


# In[15]:


#Generate a binomial distribution with n=20 and p= 0.5
binomial = np.random.binomial(20, 0.5, 1000)

#Plot a histogram
plt.hist(binomial)

#Print the histogram
plt.show()


# In[16]:


#Generate a gamma distribution with shape= 5 and scale = 1
gamma = np.random.gamma(5, 1, 1000)#5 is the shape, 1 is the scale

#Plot a histogram
plt.hist(gamma)

#Print the histogram
plt.show()


# In[17]:


#Generate a Poisson distribution witn Lambda = 3
poisson = np.random.poisson(3, 1000)

#Plot a histogram
plt.hist(poisson)

#Print the histogram
plt.show()


# ##### Distributions can also be conditional. Consider an ecommerce site. For all of the customers, we have a distribution of the amount that they have spent on the website. It may look something like this:

# In[18]:


# Creating a data frame to hold the simulated ecommerce data, and populating it with a 
#normally distributed variable w/ mean 75 and standard deviation 25.

ecommerce = pd.DataFrame()
ecommerce['spending'] = np.random.normal(75, 25, 1000)

#Plot a histogram
plt.hist(ecommerce['spending'])
plt.show()


# ##### But let's say we're actually interested in a subset of that population, for instance visitors who visited the site more than twice. That data may look like this:

# In[ ]:


# Adding a variable with counts of number of times visiting the site.
ecommerce['visit_count'] = np.random.randint(0, 5, 1000)

# Selecting only the cases where the visit count is greater than two and plotting those.
plt.hist(ecommerce[ecommerce['visit_count'] > 2]['spending'])
plt.show()


# In[19]:


#Adding a variable with counts of  number of times visiting the site
ecommerce['visit_count'] = np.random.randint(0, 5, 1000)

#Selecting only the case where the visit counts is greater than two and plotting those
plt.hist(ecommerce[ecommerce['visit_count'] > 2]['spending'])
plt.show()


# ## Drill- Descriptive Statistic and Normality

# To complete the following drills, you'll need to use your Python skills to create some datasets, then use your new statistical knowledge to summarize them. Choose 6 distributions from the list of random distributions available in NumPy, called “Distributions”
# 
# For each distribution:
# 
# Generate a random variable with 100 datapoints using the code distributionvar = np.random.distributionname([arguments], 100), replacing distributionvar with an appropriate variable name and distributionname with the name of the distribution you’ve chosen, and filling in the empty space in the parentheses with your chosen values for the appropriate parameters. If you feel uncertain about how to do this, go back to the “Other Distributions” assignment for examples of code to use as a starting point.
# Graph the variable using a histogram.
# Compute the mean and standard deviation and plot them as vertical lines on the histogram. (Hint: the “When Does It Break?” assignment you just completed can help you here.)
# Evaluate whether the descriptive statistics provided useful information about the variable. Can you identify any common characteristics of the distributions that could be usefully described using the mean and/or standard deviation, versus the ones that could not?
# Additionally:
# 
# Generate two normally-distributed variables, one with a mean of 5 and standard deviation of 0.5, and the other with a mean of 10 and standard deviation of 1.
# Add them together to create a third variable.
# Graph the third variable using a histogram.
# Compute the mean and standard deviation and plot them as vertical lines on the histogram.
# Evaluate the descriptive statistics against the data.

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 1Generate a random variable with 100 datapoints using the code distributionvar = np.random.distributionname([arguments], 100), replacing distributionvar with an appropriate variable name and distributionname with the name of the distribution you’ve chosen, and filling in the empty space in the parentheses with your chosen values for the appropriate parameters. If you feel uncertain about how to do this, go back to the “Other Distributions” assignment for examples of code to use as a starting point.

# In[3]:


#1
chisquare = np.random.chisquare(50, 100)
plt.hist(chisquare)
plt.show()


# In[6]:


print(chisquare.mean())
print(chisquare.std())


# In[5]:


#Plot a histogram for chisquare.
plt.hist(chisquare, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(chisquare.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(chisquare.mean()+chisquare.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(chisquare.mean()-chisquare.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# chisquare is normal, the mean is placed where the data clusters, with approximately 50% of the data falling on either side, and approximately 67% of the data falling within one standard deviation of the mean. 

# In[8]:


#2
#loc, scale = 0, 1
laplace = np.random.laplace(0, 1, 100)
plt.hist(laplace)
plt.show()


# In[9]:


print(laplace.mean())
print(laplace.std())


# In[12]:


#Plot a histogram for laplace.
plt.hist(laplace, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(laplace.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(laplace.mean()+laplace.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(laplace.mean()-laplace.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# Laplace is normal, the mean is placed where the data clusters, with approximately 50% of the data falling on either side, and approximately 67% of the data falling within one standard deviation of the mean. 

# In[9]:


#3
#loc, scale = 10, 1
logistic = np.random.logistic(0, 1, 100)
plt.hist(logistic)
plt.show()


# In[10]:


print(logistic.mean())
print(logistic.std())


# In[15]:


#Plot a histogram for logistic.
plt.hist(logistic, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(logistic.mean(), color = 'y', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(logistic.mean()+logistic.std(), color = 'pink', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(logistic.mean()-logistic.std(), color = 'pink', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# Logistic is normal, the mean is placed where the data clusters, with approximately 50% of the data falling on either side, and approximately 67% of the data falling within one standard deviation of the mean. 

# In[23]:


#4
ngood, nbad, nsamp = 100, 2, 10
# number of good, number of bad, and number of samples
hypergeometric = np.random.hypergeometric(ngood, nbad, nsamp, 100)
plt.hist(hypergeo)
# note that it is very unlikely to grab both bad items


# In[24]:


print(hypergeometric.mean())
print(hypergeometric.std())


# In[25]:


#Plot a histogram for hypergeometric.
plt.hist(hypergeometric, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(hypergeometric.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(hypergeometric.mean()+hypergeometric.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(hypergeometric.mean()-hypergeometric.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# For hypergeometric, the mean is still placed where the data clusters, but the cluster is not centered, and the standard deviation does not encompass the same amount of data on each side of the mean. Put another way, for rand2 the mean is no longer a measure of "central" tendency, as it does not fall in the center, and the standard deviation no longer describes how much variance there is. Asymmetric probability distributions are described as "skewed."

# In[22]:


#5
#mu, beta = 0, 0.1 # location and scale
gumbel = np.random.gumbel(0,0.1, 100)
plt.hist(gumbel)
plt.show()


# In[92]:


print("mean: ", gumbel.mean())
print("standard deviation: ",gumbel.std())


# In[23]:


#Plot a histogram for gumbel.
plt.hist(gumbel, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(gumbel.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(gumbel.mean()+gumbel.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(gumbel.mean()-gumbel.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# Logistic is gumbel, the mean is placed where the data clusters, with approximately 50% of the data falling on either side, and approximately 67% of the data falling within one standard deviation of the mean. 

# In[25]:


geometry = np.random.geometric(p=0.40, size=100)
plt.hist(geometry)
plt.show()


# In[28]:


#Plot a histogram for Geometry.
plt.hist(geometry, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(geometry.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(geometry.mean()+geometry.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(geometry.mean()-geometry.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# For Geometry, the mean is still placed where the data clusters, but the cluster is not centered, and the standard deviation does not encompass the same amount of data on each side of the mean. Put another way, for the mean is no longer a measure of "central" tendency, as it does not fall in the center, and the standard deviation no longer describes how much variance there is. Asymmetric probability distributions are described as "skewed."

# Additionally:
#  1. Generate two normally-distributed variables, one with a mean of 5 and standard deviation of 0.5, 
# and the other with a mean of 10 and standard deviation of 1.  
#  2. Add them together to create a third variable.
#  3. Graph the third variable using a histogram.
#  4. Compute the mean and standard deviation and plot them as vertical lines on the histogram.
#  5. Evaluate the descriptive statistics against the data

# In[4]:


import numpy as np 
import matplotlib.pyplot as plt

var1 = np.random.normal(5 , .5, 100)
var2 = np.random.normal(10, 1, 100)
var3 = var1 + var2

mean = np.mean(var3)
sd = np.std(var3)

plt.hist(var3)
plt.axvline(x=mean, color= 'black')
plt.axvline(x=mean+sd, color= 'red', linestyle = 'dashed')
plt.axvline(x=mean-sd, color= 'red', linestyle = 'dashed')
plt.show()


# var 3 is looks normal but results will vary depending on random seed.  In general, stats should show some skew.

# In[109]:


rand1 = np.random.normal(50, 300, 1000)
rand2 = np.random.poisson(1, 1000)
rand3 = rand1 + rand2

#Plot a histogram for rand1.
plt.hist(rand3, bins = 20, color = 'c')

#Add a vertical line at the mean
plt.axvline(rand3.mean(), color = 'b', linestyle = 'solid', linewidth= 2)

#Add a vertical line at one standard deviation above the mean.
plt.axvline(rand3.mean()+rand3.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Add a vertical line at the standard deviation below the mean.
plt.axvline(rand3.mean()-rand3.std(), color = 'b', linestyle = 'dashed', linewidth= 2)

#Print the Histogram
plt.show()


# ### Central Limit Theorem

# In[5]:


import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 1. Increase the size of your sample from 100 to 1000, then calculate the means and standard deviations for your sample and create histograms for each. Repeat this again, decreasing the size of your sample to 20. What values change, and what remain the same?
# 2. Change the population value p for group 1 to 0.3, then take new samples and compute the t-statistic and p-value. Then change the population value p for group 1 to 0.4, and do it again. What changes, and why?
# 3. Change the distribution of your population from binomial to a distribution of your choice. Do the sample mean values still accurately represent the population values?

# Let’s spin up some population data and give this a try. We’ll make two variables to represent two different populations: one a binomially distributed variable with p of 0.2, n=10, and 10000 datapoints (group1), and another binomially distributed variable with p of 0.5, n=10, and 10000 datapoints (group2). The true population difference between the two populations is 0.3.

# In[6]:


pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

# Let's make histogram for the two groups.
plt.hist(pop1, alpha= 0.5, label= 'Population 1')
plt.hist(pop2, alpha= 0.5, label= 'Population 2')
plt.legend(loc= 'upper right')
plt.show()


# The populations are not normal. Next, take a sample of 100 from each population and plot them.

# In[7]:


sample1= np.random.choice(pop1, 100, replace= True)
sample2= np.random.choice(pop2, 100, replace= True)

plt.hist(sample1, alpha= 0.5, label= 'sample 1')
plt.hist(sample2, alpha= 0.5, label= 'sample 2')
plt.legend(loc= "upper right")
plt.show()


# In[11]:


print('sample1.mean: ', sample1.mean())
print('sample2.mean: ', sample2.mean())
print('sample1.std: ', sample1.std())
print('sample2.std: ', sample2.std())

#Compute the difference between the two sample means.
diff= sample2.mean()-sample1.mean()
print('sample means diff: ', diff)


# In[143]:


size= np.array([len(sample1), len(sample2)])
sd= np.array([sample1.std(), sample2.std()])
print(size)
print(sd)


# In[144]:


size= np.array([len(sample1), len(sample2)])
sd= np.array([sample1.std(), sample2.std()])

#The squared standard deviation are divided by the sample size and summed, then we take
#square root of the sum.
diff_se= (sum(sd**2/size))**0.5

#The squared standard deviations are divided by the standard error: T-value
print(diff/diff_se)


# In[145]:


from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var= False))


# ## Drill- Exploring the Central limit theorem

# In[1]:



import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 1. Increase the size of your sample from 100 to 1000, then calculate the means and standard deviations for your sample and create histograms for each. Repeat this again, decreasing the size of your sample to 20. What values change, and what remain the same?
# 
# 2. Change the population value p for group 1 to 0.3, then take new samples and compute the t-statistic and p-value. Then change the population value p for group 1 to 0.4, and do it again. What changes, and why?
# 
# 3. Change the distribution of your population from binomial to a distribution of your choice. Do the sample mean values still accurately represent the population values?

# In[13]:


# Sample sizes 100
pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

print('sample1.mean: ', sample1.mean())
print('sample2.mean: ', sample2.mean())
print('sample1.std: ', sample1.std())
print('sample2.std: ', sample2.std())

# Compute the difference between the two sample means.
diff=sample2.mean( ) - sample1.mean()
print('diff_sample1_2: ', diff)

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 
plt.show()


# In[14]:


# Sample sizes 1000
pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 1000, replace=True)
sample2 = np.random.choice(pop2, 1000, replace=True)

print('sample1.mean: ', sample1.mean())
print('sample2.mean: ', sample2.mean())
print('sample1.std: ', sample1.std())
print('sample2.std: ', sample2.std())

# Compute the difference between the two sample means.
diff=sample2.mean( ) -sample1.mean()
print('diff_sample1_2: ', diff)

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 
plt.show()


# Sample sizes 20
# pop1 = np.random.binomial(10, 0.2, 10000) 
# pop2 = np.random.binomial(10,0.5, 10000)
# 
# sample1 = np.random.choice(pop1, 20, replace=True) 
# sample2 = np.random.choice(pop2, 20, replace=True)
# 
# print(sample1.mean()) print(sample2.mean()) print(sample1.std()) print(sample2.std())

# In[15]:


# Sample sizes 20
pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 20, replace=True)
sample2 = np.random.choice(pop2, 20, replace=True)

print('sample1.mean: ', sample1.mean())
print('sample2.mean: ', sample2.mean())
print('sample1.std: ', sample1.std())
print('sample2.std: ', sample2.std())

# Compute the difference between the two sample means.
diff=sample2.mean( ) -sample1.mean()
print('diff_sample1_2: ', diff)

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 
plt.show()


# In[ ]:


#sample size 20
mean1:  2.15
mean2:  5.6
standard1:  1.2757350822173075
standard2:  1.3564659966250538
diff_sample1_2:  3.4499999999999997

#sample size 100
mean1:  2.05
mean2:  4.8
standard1:  1.1434596626029272
standard2:  1.4560219778561037
diff_sample1_2:  2.75
    
#sample size 1000
mean1:  2.046
mean2:  4.995
standard1:  1.3160106382548737
standard2:  1.5661976248226148
diff_sample1_2:  2.9490000000000003

#Means has a little changes, Standard deviation changes more.


# 2. Change the population value p for group 1 to 0.3, then take new samples and compute the t-statistic and p-value. Then change the population value p for group 1 to 0.4, and do it again. What changes, and why?

# In[14]:


# Pop1 p = .3
pop1 = np.random.binomial(10, 0.3, 10000)
pop2 = np.random.binomial(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))


# In[13]:


# Pop1 p = .4
pop1 = np.random.binomial(10, 0.4, 10000)
pop2 = np.random.binomial(10,0.5, 10000) 


sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))


# In[ ]:


# 2. The t-value shrinks and the p-value gets larger as the samples become more similar


# 3. Change the distribution of your population from binomial to a distribution of your choice. Do the sample mean values still    accurately represent the population values?

# ### Use gamma distribution

# In[4]:


# Sample size 1000
pop1 = np.random.gamma(10, 0.3, 10000)
pop2 = np.random.gamma(10, 0.5, 10000)


sample1 = np.random.choice(pop1, 1000, replace = True)
sample2 = np.random.choice(pop2, 1000, replace = True)


print('mean1: ', sample1.mean())
print('mean2: ', sample2.mean())
print('standard1: ', sample1.std())
print('standard2: ', sample2.std())

#Compute the difference between the two sample means.
diff= sample2.mean() - sample1.mean()
print('diff_sample1_2: ', diff)

plt.hist(sample1, alpha=0.5, label= 'sample 1')
plt.hist(sample2, alpha= 0.5, label= 'sample2')
plt.legend(loc= 'upper right')
plt.show


# In[6]:


# Sample size 20
pop1 = np.random.gamma(10, 0.3, 10000)
pop2 = np.random.gamma(10, 0.5, 10000)


sample1 = np.random.choice(pop1, 20, replace = True)
sample2 = np.random.choice(pop2, 20, replace = True)


print('mean1: ', sample1.mean())
print('mean2: ', sample2.mean())
print('standard1: ', sample1.std())
print('standard2: ', sample2.std())

#Compute the difference between the two sample means.
diff= sample2.mean() - sample1.mean()
print('diff_sample1_2: ', diff)

plt.hist(sample1, alpha=0.5, label= 'sample 1')
plt.hist(sample2, alpha= 0.5, label= 'sample2')
plt.legend(loc= 'upper right')
plt.show


# In[7]:


# Pop1 p = .3
pop1 = np.random.gamma(10, 0.3, 10000)
pop2 = np.random.gamma(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 1000, replace=True)
sample2 = np.random.choice(pop2, 1000, replace=True)

from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))


# In[16]:


# Pop1 p = .3
pop1 = np.random.gamma(10, 0.3, 10000)
pop2 = np.random.gamma(10,0.5, 10000) 

sample1 = np.random.choice(pop1, 20, replace=True)
sample2 = np.random.choice(pop2, 20, replace=True)

from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))


# In[ ]:


use Gamma distribution
# Sample size 1000
mean1:  3.0190556439983656
mean2:  5.0046588053553025
standard1:  0.949050890472955
standard2:  1.603432721570148
diff_sample1_2:  1.985603161356937
Ttest_indResult(statistic=32.80005477154023, pvalue=1.437580338140222e-181)

# Sample size 20    
mean1:  3.0365267090523966
mean2:  4.931741308939336
standard1:  0.7615609569691818
standard2:  1.3332407686653676
diff_sample1_2:  1.8952145998869394
Ttest_indResult(statistic=4.4773448635040305, pvalue=9.646624383002043e-05)


# 3. The Central Limit Theorem says the statistics should still work as long as the sample size is large enough, 
#    no matter what distribution is chosen

# p-value 
#     -This tells us how likely it is that we would get the sampling data we observe if the two population means were not, in fact, different from one another. 
#     -The lower the p-value, the more confidently we can conclude that there is a meaningful difference between the means of the two groups in the population.
# The t-value 
#     -scales the difference between the two groups by the amount of variance in the two samples.
#     -One way to interpret a t-value is as the number of standard errors worth of space separating the group means. A t-value of 2 would indicate that the means are two standard errors apart.
