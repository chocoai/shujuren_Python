
# coding: utf-8

# # Python3 sklearn 集成学习方法
# 
# 三种方法：
# 
# - 1 Bagging算法，包括：Bagged Decision Trees,Random Forest, Extra Trees
# 
# - 2 Boosting算法, 包括：AdaBoost和Stochastic Gradient Boosting
# 
# - 3 Voting 算法

# ## Bagging Algorithms

# ### 1 Bagged Decision Trees 

# In[1]:


import pandas as pd
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier


# In[2]:


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']


# In[3]:


df = pd.read_csv(url, names=names)


# In[4]:


array = df.values


# In[5]:


X = array[:,0:8]
Y = array[:,8]


# In[6]:


seed = 7
kfold = KFold(n_splits=10, random_state=seed)
cart = DecisionTreeClassifier()


# In[8]:


num_trees = 100
model = BaggingClassifier(base_estimator=cart, n_estimators=num_trees, random_state=seed)


# In[9]:


from sklearn.model_selection import cross_val_score


# In[10]:


results = cross_val_score(model, X, Y, cv=kfold)


# In[11]:


print(results)


# In[12]:


print(results.mean())


# ### 2 Random Forest

# In[13]:


from sklearn.ensemble import RandomForestClassifier


# In[14]:


max_features = 3


# In[15]:


RF_model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features, random_state=seed)


# In[22]:


RF_results = cross_val_score(RF_model, X, Y, cv=kfold)  


# In[23]:


print(RF_results.mean())


# ### 3 Extra Trees

# In[18]:


from sklearn.ensemble import ExtraTreesClassifier


# In[19]:


max_features1 = 7


# In[20]:


ET_model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features1)


# In[21]:


ET_results = cross_val_score(ET_model, X, Y, cv=kfold)


# In[24]:


print(ET_results.mean())


# ## Boosting Algorithms 

# ### 1 AdaBoost

# In[25]:


from sklearn.ensemble import AdaBoostClassifier


# In[26]:


adaboost_model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)


# In[27]:


adaboost_results = cross_val_score(adaboost_model, X, Y, cv=kfold)


# In[28]:


print(adaboost_results.mean())


# ###  2 Stochastic Gradient Boosting

# In[29]:


from sklearn.ensemble import GradientBoostingClassifier


# In[30]:


sgb_model = GradientBoostingClassifier(n_estimators=num_trees, random_state=seed)


# In[31]:


sgb_results = cross_val_score(sgb_model, X, Y, cv=kfold)


# In[32]:


print(sgb_results.mean())


# ##  Voting Ensemble

# In[33]:


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier


# In[34]:


estimators = []


# In[35]:


LR_model = LogisticRegression()


# In[36]:


estimators.append(('LR', LR_model))


# In[37]:


CART_model = DecisionTreeClassifier()


# In[38]:


estimators.append(('CART', CART_model))


# In[39]:


SVC_model = SVC()


# In[40]:


estimators.append(('SVC', SVC_model))


# In[41]:


ensemble_model = VotingClassifier(estimators)


# In[42]:


voting_results = cross_val_score(ensemble_model, X, Y, cv=kfold)


# In[43]:


print(voting_results.mean())

