
# coding: utf-8

# In[1]:

#50  amostras  de 3  especies  diferentes  de íris  (150 amostras  no total)
#medidas: comprimento  sepal, largura sepal,  comprimento  da pétala,largura da pétala 

from IPython.display import IFrame
IFrame('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', width=300, height=200)


# In[2]:

#importar  load_iris função  do módulo  de conjuntos  de dados 
from sklearn.datasets import load_iris


# In[3]:

#Salvar  o objeto "bunch" contendo o conjunto  de dados  da íris  e seus 
#atributos 
iris = load_iris()
type(iris)


# In[5]:

#imprimir os dados iris 
print(iris.data)


# In[7]:

#imprimir  os nomes  dos quatro  recursos de medidas 
print (iris.feature_names)


# In[8]:

#imprime  números  inteiros  que representam as espécies de cada observação
print(iris.target)


# In[9]:

#imprima  o esquena  de codificação para espécies : 0 = setosa , 1= versicolor ,
#2 = virginica 

print(iris.target_names)


# In[12]:

# verifica tipos de recursos e resposta
print(type(iris.data))
print(type(iris.target))


# In[14]:

#verificar as formas de recursos 
# (primeira dimensão = número de observações, segundas dimensões = número de recursos)
print(iris.data.shape)


# In[16]:

# verifica a forma da resposta(uma  única  dimensão que corresponde ao  numero  de observação)
print(iris.target.shape)


# In[19]:

#matriz   de recursos da loja em 'X'

x =iris.data

#vetor  de resposta  da loja  em "y"
y = iris.target


# In[ ]:



