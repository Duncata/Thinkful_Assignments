#!/usr/bin/env python
# coding: utf-8

# ## Exploring the Dataset

# NCHS - Leading Causes of Death: United States
# Metadata Updated: February 28, 2019 
# 
# This dataset presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999. Data are based on information from all resident death certificates filed in the 50 states and the District of Columbia using demographic and medical characteristics. Age-adjusted death rates (per 100,000 population) are based on the 2000 U.S. standard population. Populations used for computing death rates after 2010 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Causes of death classified by the International Classification of Diseases, Tenth Revision (ICD–10) are ranked according to the number of deaths assigned to rankable causes. Cause of death statistics are based on the underlying cause of death. SOURCES CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov). REFERENCES
# 
# National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.
# 
# Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. Deaths: Final data for 2015. National vital statistics reports; vol 66. no. 6. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.

# 2000 U.S. Standard Population Age Groups
# The population used to age-adjust the rates in this report is the 2000 U.S. standard population.1 2 On this website, the 2000 U.S. standard population is based on the proportion of the 2000 population in 19 specific age groups (younger than 1 year, 1–4 years, 5–9 years, 10–14 years, 15–19 years, … 85 years and older); except for Puerto Rico, where it is based on 18 specific age groups (0–4 years, 5–9 years, 10–14 years, 15–19 years, … 85 years and older); the proportions of the 2000 population in these age groups serve as weights for calculating age-adjusted incidence and death rates. Cancer death rates on this website may differ slightly from those published by the National Center for Health Statistics (NCHS) because NCHS uses age groups as recommended by the U.S. Department of Health and Human Services in its adjustment of death rates. In addition, the 2000 U.S. standard population weights are not race- or sex-specific, so they do not adjust for differences in race or sex distribution between geographic areas or populations being compared. They do, however, provide the basis for adjusting for differences in the age distributions across groups defined by sex, race, geography, or other categories.

# https://www.healthline.com/health/leading-causes-of-death(Tells more about the project)

# https://www.youtube.com/watch?v=umg5tP5-kRo  (explain adjusted death of rate)

# 1. A "standard" population distribution is used to adjust death and hospitalization rates. The age-adjusted rates are rates that would have existed if the population under study had the same age distribution as the "standard" population. Therefore, they are summary measures adjusted for differences in age distributions.
# 
# 2. To calculate the age-standardized mortality rate (ASMR), we must first calculate the age-specific (mortality) rates for each age group by dividing the number of deaths by the respective population, and then multiplying the resulting number by 100,000: Age-specific rate, 0 to 39 years.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Read in data into dataframe
df_LCDUS= pd.read_csv('Downloads/NCHS_-_Leading_Causes_of_Death__United_States.csv')
df_LCDUS.head()


# In[3]:


# overwrite the current setting so that more characters will be displayed
pd.set_option('display.max_colwidth', 1000)
df_LCDUS.head()


# In[4]:


#See how many index and columns
df_LCDUS.shape


# In[5]:


#Check for null or empty rows/columns
df_LCDUS.isna().sum()


# In[6]:


# We remove a single column (axis=1 refers to columns) cause it is the same with cause_name
df_LCDUS.drop('113 Cause Name', axis=1, inplace=True)


# In[7]:


#check how many rows and column
df_LCDUS.shape


# In[45]:


# replace all spaces with underscores and all small letter in the column names by using the 'str.replace' method,
# this will help in commands later(example: df_LCDUS.age_adjusted_death_rate.describe())

df_LCDUS.columns = df_LCDUS.columns.str.replace(' ', '_').str.replace('-', '_').str.lower()
df_LCDUS.columns


# In[9]:


#Add new columns population by computing it from number of death 
#and Age-adjusted death rates (per 100,000 population) are based on the 
#2000 U.S. standard population.


df_LCDUS['population'] = (df_LCDUS['deaths']*100000) / df_LCDUS['age_adjusted_death_rate']
df_LCDUS.head()


# This link will explain more about age_adjusted_death_rate (https://www.youtube.com/watch?v=umg5tP5-kRo ) 
# or (https://www.youtube.com/watch?v=cr1UT-d9VJw)

# In[10]:


#check types of columns variable
df_LCDUS.dtypes


# In[12]:


#Check the change on the columns names
df_LCDUS.head()


# In[13]:


#The method describe int & float
df_LCDUS.describe()


# In[ ]:





# ### Let us explore first the column Deaths

# In[14]:


#Let Find 1st the cause_name, acronym CLRD means Chronic Lower Respiratory disease
df_LCDUS.cause_name.unique()


# In[ ]:





# ### GROUP BY CAUSE NAME

# In[15]:


#calculate the mean, min, max deaths using aggregate function in each cause_name
df_LCDUS.groupby('cause_name').deaths.agg(['mean', 'min', 'max', 'sum'])


# In[16]:


#For now, we study only the death cause by disease so we remove All causes, Suicide, Unintentional injuries. 
#All causes number is way to high and have effect on our data. 


# In[17]:


#Python will retain only the boolean 'True' when reading the column cause_name by row.

df_diseases = df_LCDUS[(df_LCDUS.cause_name != 'All causes') & 
                        (df_LCDUS.cause_name !='Unintentional injuries') & 
                        (df_LCDUS.cause_name !='Suicide')]

df_diseases.head()


# In[18]:


df_diseases.cause_name.value_counts()


# In[19]:


#Check it, we can see now that the row reduce from 10296 to 7488.
df_diseases.shape


# In[20]:


#Now we visualize the mean deaths in each cause_name
grpby_coznm_death = df_diseases.groupby('cause_name').deaths.mean()
grpby_coznm_death.head(10)


# In[21]:


#Check the type if series or dataframe cause there are different commands for each.
type(grpby_coznm_death)


# ### See the number of cause of death by Visualization

# In[22]:



grpby_coznm_death.plot(kind='bar', figsize=[15,5])
plt.ylabel('Number')
plt.xlabel('Name of Disease')
plt.title('NUMBER OF MEAN DEATHS IN EACH DISEASE')


# In[23]:


#The histogram shows the possible values of a variables, as well as how common those values are.
#the frequency of the data/Dist of data
plt.hist(grpby_coznm_death, color='red')
plt.title('')
plt.ylabel('frequency')
plt.show()


# In[24]:


plt.boxplot(grpby_coznm_death)


# ## What year have the highest death?

# In[25]:


#Now we visualize the sum deaths in each Year
grpby_yr_death = df_diseases.groupby('year').deaths.agg(['mean', 'min', 'max', 'sum']) 
grpby_yr_death


# In[26]:


grpby_yr_death_sum=df_diseases.groupby('year').deaths.sum()
grpby_yr_death_sum


# In[ ]:





# In[27]:


#Line Plot
plt.plot(grpby_yr_death_sum)
#plt.xlim([1997, 2017])
plt.ylabel('Number of Deaths')
plt.xlabel('Year')
plt.title('NUMBER OF MEAN DEATHS IN EACH YEAR')


# In[28]:


grpby_yr_death_sum.plot(kind='bar', figsize=[15,5], ylim=(3100000, 3800000))
plt.ylabel('Number of Deaths')
plt.xlabel('Year')
plt.title('NUMBER OF MEAN DEATHS IN EACH YEAR')


# In[29]:


#grpby_year_death.plot(kind='hist', figsize=[15,5])
#plt.ylim([14000, 17000])
#plt.ylabel('Value')
plt.hist(grpby_yr_death_sum)# vis. the frequency of the data/Dist of data


# In[30]:



plt.boxplot(grpby_yr_death_sum)


# ### GROUP BY STATE
# 

# ### What State have the highest Death?

# In[31]:


grpby_state_death = df_diseases.groupby('state').deaths.agg(['mean', 'min', 'max', 'sum'])
grpby_state_death


# In[32]:


grpby_state_death.plot(kind='bar', figsize=[15,5])
plt.ylabel('Value')


# In[33]:


#Remove the outlier United States
df_states = df_diseases[df_diseases.state != 'United States']
df_states


# In[34]:


df_states.year.unique()


# In[35]:


grpby_states_deaths_mean = df_states.groupby('state').deaths.mean()
grpby_states_deaths_mean


# In[36]:


type(grpby_states_deaths_mean)


# In[37]:


grpby_states_deaths_mean.sort_values().plot(kind='bar', figsize=[15,5])
#plt.ylim([14000, 17000])
plt.ylabel('Value')


# In[ ]:





# In[38]:


plt.plot(grpby_states_deaths_mean)


# In[ ]:





# In[39]:


plt.boxplot(grpby_states_deaths_mean)


# In[40]:


#shows the distribution of a numerical variable
plt.hist(grpby_states_deaths_mean)


# In[ ]:





# ### Death of heart disease per state

# In[41]:


df_hrt_dis= df_states[df_states['cause_name'] == 'Heart disease']
df_hrt_dis.head()


# In[42]:


df_hrt_dis.groupby('state').deaths.sum().sort_values().plot(kind= 'bar', figsize=[15,5])


# In[43]:



def dis_per_states(x):
    for n in df_states['cause_name'].unique():
        
        if n == x:
            df_dis= df_states[df_states['cause_name'] == x]
    
            return df_dis.groupby('state').deaths.sum().sort_values().plot(kind= 'bar', figsize=[15,5])
    
        
            


# In[44]:


death_state('Heart disease')


# In[ ]:


death_state('Influenza and pneumonia')


# In[ ]:


death_state("Alzheimer's disease")


# In[ ]:


death_state("Kidney disease")


# In[ ]:


death_state("CLRD")


# In[ ]:


df_states.cause_name.unique()


# In[ ]:


df_states.head()


# In[ ]:


df_states.tail()


# In[ ]:


df_states.shape


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats

from IPython import display
from ipywidgets import interact, widgets

get_ipython().run_line_magic('matplotlib', 'inline')

import re
import mailbox
import csv


# In[ ]:


df_states[df_states.year == 1999].plot.scatter('population','age_adjusted_death_rate')


# In[ ]:


def plotyear(year):
    data = df_states[df_states.year == year]
    area = 5e-3 * data.deaths
    colors = data['cause_name'].map({"Alzheimer's disease":'green',
       'Cancer':'violet', 'CLRD':'yellow', 'Diabetes':'pink', 'Heart disease':'red',
       'Influenza and pneumonia':'coral', 'Kidney disease':'brown', 'Stroke':'palegreen'})
    
    data.plot.scatter('population', 'age_adjusted_death_rate', s = area, c = colors)

plotyear(1999)


# In[ ]:


interact(plotyear, year=widgets.IntSlider(min=1999, max=2016, step=1, value= 1999))


# In[ ]:


df_states[df_states.year == year]


# Highlights
# Mortality experience in 2015
# • In 2015, a total of 2,712,630 resident deaths were
# registered in the United States, yielding a crude death rate of
# 844.0 per 100,000 population.
# • The age-adjusted death rate, which accounts for the aging
# of the population, was 733.1 deaths per 100,000 U.S.
# standard population.
# • Life expectancy at birth was 78.8 years.
# • The 15 leading causes of death in 2015 were:
# 1. Diseases of heart (heart disease)
# 2. Malignant neoplasms (cancer)
# 3. Chronic lower respiratory diseases
# 4. Accidents (unintentional injuries)
# 5. Cerebrovascular diseases (stroke)
# 6. Alzheimer’s disease
# 7. Diabetes mellitus (diabetes)
# 8. Influenza and pneumonia
# 9. Nephritis, nephrotic syndrome and nephrosis (kidney
# disease)
# 10. Intentional self-harm (suicide)
# 11. Septicemia
# 12. Chronic liver disease and cirrhosis
# 13. Essential hypertension and hypertensive renal disease (hypertension)
# 14. Parkinson’s disease
# 15. Pneumonitis due to solids and liquids 
