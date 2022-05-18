#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Data Processing

# In[2]:




covid_data=pd.read_csv("/Users/mac/Desktop/covid19.csv")


# In[3]:


covid_data.head() #to get the first five dataset


# In[4]:


covid_data.tail() #to get the last 5 data from the data set


# In[5]:


covid_data.shape #to get the total number of rows and columns


# In[6]:


covid_data.dtypes #to find the Datatypes


# In[7]:


covid_data.info() #to get all the information about our dataset


# In[8]:


covid_data.isnull().sum() #to find the null values


# In[9]:


sns.heatmap(covid_data.isna()) #To visualise the null values in dataset


# # Data Cleaning

# In[10]:


#For our convinenece we can just rename our column names


# In[11]:


covid_data.rename(columns={'id':'id','Region of residence':'region',
        'Age of Subject': 'age',
        'Time spent on Online Class': 'time_online_class',
        'Rating of Online Class experience': 'rating_online_class',
        'Medium for online class': 'medium',
        'Time spent on self study': 'time_self_study',
        'Time spent on fitness': 'time_fitness',
        'Time spent on sleep': 'time_sleep',
        'Time spent on social media': 'time_social_media',
        'Prefered social media platform': 'prefered_social_media',
        'Time spent on TV': 'time_tv',
        'Number of meals per day': 'num_meals_per_day',
        'Change in your weight': 'weight_change',
        'Health issue during lockdown': 'health_issue_in_lockdown',
        'Stress busters': 'stress_busters',       
        'Time utilized': 'time_utilized',
        'Do you find yourself more connected with your family, close friends , relatives  ?': 'more_family_connected',
        'What you miss the most': 'miss_most'}, inplace = True)


# In[15]:


covid_data.columns


# In[12]:


covid_data['rating_online_class'].unique()   #to get the unique values in rating_online_class


# In[13]:


covid_data['rating_online_class']=covid_data['rating_online_class'].replace(np.nan,"Very poor")#to replace the nan values


# In[14]:


covid_data['medium'].unique()


# In[20]:


covid_data['medium'].value_counts()


# In[21]:


covid_data['medium']=covid_data['medium'].replace(np.nan,'Smartphone')


# In[24]:


covid_data['time_tv'].unique()


# In[25]:


covid_data['time_tv']=covid_data['time_tv'].replace({'n':'1','N':'0','No tv':'0',' ':'0' })#Replacing 'n','N','no',empty with 0
covid_data['time_tv'].value_counts()                         


# In[26]:


covid_data['time_tv'] =covid_data['time_tv'].astype('float',copy=True)  #to change  the datatype object of 
the column 'time_tv'to float to


# In[28]:


covid_data['prefered_social_media'].value_counts()


# In[29]:


covid_data['prefered_social_media'].unique()


# In[30]:


covid_data['prefered_social_media'].replace('WhatsApp','Whatsapp', inplace=True)

covid_data['prefered_social_media'].replace('None ','None',inplace=True )


# In[33]:


covid_data['stress_busters'].unique()


# In[34]:


covid_data['stress_busters'].replace([
    ['Sleep'],
    ['Scrolling through social media'],
    ['Reading books'],
    ['Talking to your relatives']
], ['Sleeping', 'Social Media', 'Reading',  'Talking'],inplace=True)


# In[35]:


covid_data['stress_busters'].replace([
    'Exercising','Exercise','Gym','Workout ','Cardio',
    'workout','working out and some physical activity'
],'Exercise/Gym', inplace=True)


# In[36]:


covid_data['stress_busters'].replace([
    'Talking with friends ','Talking','Talking to friends','With a friend',
    'Calling friends','Taking with parents','Talk with childhood friends.',
], 'Talking',inplace=True )


# In[37]:


covid_data['stress_busters'].replace([
    'Listening to music',' listening music, motion design, graphic design, sleeping.',
    'singing','Workout and listening music',
    'Both listining music and scrolling down social media',
    'Listening to music and reading books both . ',
    'Poetry, writing books and novels , listening to music too'
], 'Music' , inplace=True)


# In[38]:


covid_data['stress_busters'].replace([
    'Online surfing','live stream watching','Watching orgasm releasing videos','Anime Manga',
    'Watching ted talks and music and books','Watching YouTube ','Internet',
    'Online gaming , surfing and listening to music ','Web Series','Watching web series',
    'Netflix, Friends and Books','Youtube'
], 'Net Surfing' ,inplace=True)


# In[39]:


covid_data['stress_busters'].replace([
    'Coding and studying for exams',
    'sketching,reading books,meditation,songs',
    'Many of these',
    'All reading books watching web series listening to music and talking to friends',
    'Many among these ',
    'Do some home related stuff',
    'watching movies,reading books,games,listening to music,sleep,dancing',
    'Reading books, music, exercise',
    'Whatever want','listening to music,reading books and dancing.',
], 'Others',inplace=True)


# In[40]:


covid_data['stress_busters'].replace([
    'Sleeping, Online games',
    'pubg'
], 'Online gaming',inplace=True)


# In[41]:


covid_data['stress_busters'].replace([
    'Reading','drawing','Dancing','Meditation','Driving','Drawing, painting','Forming ','Painting','Sketching',
    'Sports','Painting ','Drawing','Football','Business','Running','I run','Drawing and painting and sketching',
    'I play Rubiks cube','Indoor Games','I cant de-stress myslef','Writing my own Comics & novels',
    'I have no problem of stress ','Sketching and writing','By engaging in my work.', 'Work',
    'Painting,. Sewing','Crying','Dont get distreessed','gardening cartoon','Playing ','no stress',
    'Cricket','No able to reduce the stress ','drawing ','Writing'],'Extra activities',inplace=True)


# In[44]:


covid_data['miss_most'].unique()


# In[ ]:





# In[45]:


covid_data['miss_most'].replace(
    [
        'All the above',
        'All of the above ',
        'everything',
        'All above',
        'all of the above',
        'ALL','all',
        'All of the above',
        'all of them',
        'All of them',
        'All '
    ],
    'All',inplace=True)


# In[46]:


covid_data['miss_most'].replace(
    [
        'NOTHING',
        'Nothing this is my usual life',
        'To stay alone. ',
        'Nothing ',
        'Nah, this is my usual lifestyle anyway, just being lazy....',
        'Normal life',
        'My normal routine',
        'nothing',
        'Job',
        'I have missed nothing',
        'Previous mistakes',
        '.','I have missed nothing','I have missed nothing '],'Nothing', inplace=True)


# In[47]:


covid_data['miss_most'].replace(
    [
        'Only friends','School/college','Colleagues',
        'Friends , relatives',
        'relatives and friends',
        'Family ',
        'The idea of being around fun loving people but this time has certainly made us all to reconnect (and fill the gap if any) with our families and relatives so it is fun but certainly we do miss hanging out with friends',
        'Family',
        'Friends, relatives & travelling',
        'Travelling & Friends',
        'School and friends',
        'Friends and School',
        'Eating outside and friends.',
        'School and friends.',
        'school, relatives and friends',
        'School and my school friends'
    ],
    'School/Friends/Family',inplace=True)


# In[48]:


covid_data['miss_most'].replace(
    [
        'Playing',
        'Roaming around freely',
        'Taking kids to park',
        'Being social ',
        'Friends and roaming around freely',
        'Friends,Romaing and traveling',
        'Metro',
        'Going to the movies',
        'Gym',
        'Football',
        'Badminton in court'
    ],
    'Outdoor activities',inplace=True)


# In[51]:


covid_data.describe()


# Here we get to know that people from age 7 to 59 are studying online during covid 19.
# 
# Average timespent on online class is 3 hours.
# 
# Average time for self study is Approx 3 hours.
# 
# Average time given to self study : 2.9 hours ~ almost 3 hours.
# 
# Average time given to fitness/health : 1 hour.
# 
# Average time spend on social media : 2.36 hours.
# 
# Average meal people are getting : nearly 3 time/day.
# 

# # Age Distribution

# In[52]:


covid_data.age.describe()


# In[53]:


sns.distplot(covid_data['age']) #visualising age


# In[54]:


sns.kdeplot(covid_data['age'])


# In[17]:


covid_data['rating_online_class'].value_counts()


# In[18]:


sns.countplot(covid_data['rating_online_class'])
plt.xticks(rotation=60)
plt.show()


# From the above scenario we can say that most of the students dont like online class.
# Students are not interested in online class as compared to actual classes

# In[22]:


covid_data['medium'].value_counts()


# In[23]:


sns.countplot(covid_data['medium'])
plt.xticks(rotation=70)
plt.show()


# Here we get that smartphone is the most prefered medium by the people

# In[27]:


sns.countplot(covid_data['time_tv'])
plt.xticks(rotation=40)
plt.show()


# Here we can understand that above 450 people doesnot spend much time using tv.
# 1 to 2 hours spend by people of 250 on avg

# In[31]:


covid_data['prefered_social_media'].value_counts()


# In[32]:



sns.countplot(covid_data['prefered_social_media'])
plt.xticks(rotation=50)
plt.show()


# From the above scenario we get to find that Instagram is the most prefered social media by people,then comes whatspp and youtube respectively.

# In[42]:


covid_data['stress_busters'].value_counts()


# In[43]:


sns.countplot(covid_data['stress_busters'])# visualising the stress busters
plt.xticks( rotation=60)
plt.show()


# Most of the students took music as their  stress busters,
# then comes netsurfing,
# doing extra activitieslike reading,writing,dancing ,singing etc as their stress relief method.
# Last but not the least online gaming is  considered as a great stress relieving way.

# In[49]:


covid_data['miss_most'].value_counts()


# In[50]:


sns.countplot(covid_data['miss_most']) #for visualising the things students missed the most.
plt.xticks(rotation=75)
plt.show()


# More than 600 people are missing their schools/friends/family, some of them are 
# missing travelling,outdoor activities,eating outside respectively.

# In[56]:


#to find whether students which region students spend more time online class 


# In[57]:


covid_data.groupby('region')['time_online_class'].sum()


# In[58]:


sns.barplot(covid_data['region'],covid_data['time_online_class'])


# Here we get to know that students in Delhi spend more time in online class

# In[59]:


#Which medium is used the most?


# In[60]:


covid_data.groupby(['medium']).mean()


# In[ ]:





# In[61]:


#Visualising through barplot the health issue in lockdown and fitness


# In[62]:


sns.barplot(covid_data.health_issue_in_lockdown,covid_data.time_fitness,hue=covid_data.health_issue_in_lockdown)
plt.title('Barplot',fontsize=20)
#plt.xlabel(f)
plt.legend(loc='upper right')
plt.show()


# In[63]:


covid_data.groupby('health_issue_in_lockdown').mean().plot(
    kind='pie',y='time_fitness', autopct='%1.0f%%')


# In[64]:


sns.barplot(covid_data.region,covid_data.time_social_media)


# # Weight change on students

# In[65]:


covid_data.columns


# In[66]:


covid_data['weight_change'].value_counts()


# In[16]:



labels=covid_data['weight_change'].value_counts().index
colors=['blue','red','green']
sizes=covid_data['weight_change'].value_counts().values
plt.figure(figsize=(7,7))
plt.title('Weight change on students',fontsize=20)
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
plt.legend(['Remain Constant','Increased','Decreased'],loc=1)
plt.show()


# In[ ]:


45.3%  says that there is no change in weight during lockdown(covid 19).
37.1% students tell that they gained weight during the pandemic lockdown.
17.7% says that they had lost their weight.


# In[76]:


#countplot of weight change which gives the visualisation in counts
sns.countplot(covid_data['weight_change']) 


# # Weight change and number of meals

# In[80]:


x=covid_data['weight_change']
y=covid_data['num_meals_per_day']
plt.xlabel('weight_change')
plt.ylabel('num_meals_per_day')
plt.title('barplot',fontsize=10)
plt.bar(x,y,width=0.5)


# Here we get to understand that the students who eats more gain more weight.
# Some of them dont have any change in their weight, they remains constant.
# As their num of meals are less then they will have decreased weight.

# In[86]:


#boxplot to see outliers
plt.figure(figsize=(12,8))
sns.set(style='darkgrid')
sns.boxplot(y='weight_change', x='num_meals_per_day', data=covid_data)
plt.show()


# # Weight  change and time sleep

# In[90]:


covid_data.columns


# In[95]:


x=covid_data['weight_change']
y=covid_data['time_sleep']
plt.title('Barplot',fontsize=10)
plt.xlabel('weight_change')
plt.ylabel('time_sleep')
plt.bar(x,y,width=0.3,color='g')


#  The students who sleep more than 14 hours have an increased weight 

# In[81]:


#to get the correlation
covid_data.corr()


# In[84]:


#visualising the correlation using heatmap
sns.heatmap(covid_data.corr(),annot=True)
plt.figure(figsize=(10,10))
plt.show()


# # Inferences and conclusion

# In[ ]:


Here is the some inferences and conclusions I made from this dataset.

Most of the students answered the questions of the survey.according to the rating of online class  ,
most of the students dont like online class ,they like active offline classes.

According to the data ,50% of the students use smartphone as their medium for online class.

Now in Social Media prespective we found that Instagram and WhatsApp are the most popular among
Students which is quite expected.

 Majority of the students feel more connected to their family/close friends because lockdown 
    has given them opportunity to spend quality time guring pandemic.
    
According to the data Students are missing School and College the most during 
pandemic lockdown.


 We Also found out that about 45% students reported no change in their weight whereas
    37% reported a weight gain and 
    18% students reported weight loss.

    Finally we infer that Music is the best Stress-Busters 
    among students followed by Extra-Activities 

