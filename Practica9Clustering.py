import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Agrupamiento de datos (Clustering) K-Means

df = pd.read_csv("csv/netflix_catalogo_drama.csv")
dat_kmeans = df.drop(columns=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','rating', 'duration', 'listed_in', 'description'])
#print(dat_kmeans.describe())
#print(dat_kmeans.groupby('rating_id').size())
#dat_kmeans.drop(['rating_id'],1).hist()
#sb.pairplot(dat_kmeans.dropna(), hue='rating_id',height=3,vars=["type_id","country_digit","release_year"],kind='scatter')
X = np.array(dat_kmeans[["country_digit", "type_id", "release_year"]])
y = np.array(dat_kmeans['rating_id'])
Nc = range(1, 20)

kmeans = [KMeans(n_clusters=i) for i in Nc]
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
#plt.plot(Nc,score)
#plt.xlabel('Numero de Clusters')
#plt.ylabel('Score')
#plt.title('Elbow Curve')
#plt.show() # Número de clusters = 2 a 5

kmeans = KMeans(n_clusters=4).fit(X)
centroids = kmeans.cluster_centers_
#print(centroids)
# Predecir clusters
labels = kmeans.predict(X)
# Obtener los centros de los cluster
C = kmeans.cluster_centers_
colors = ['maroon', 'lime', 'cyan', 'darkorange']
colores=['red', 'green', 'blue', 'yellow']
asignar=[]
for row in labels:
    asignar.append(colores[row])
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colors, s=1000)
#plt.savefig('img/plot_classification_3d.png')

# Conseguir los datos y plotearlos
f1 = dat_kmeans['type_id'].values
f2 = dat_kmeans['release_year'].values
plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()
#plt.savefig('img/plot3_datos.png')
plt.close()

#df_rating = pd.read_csv("csv/catalogo_rating_drama.csv")
#print(df["rating_id"])
#for i in df.index:
    #j = 0
    #for j in df_rating.index:
        #if df["rating"][i] == df_rating["rating"][j]:
        #    df["rating_id"][i] = j
#print(df["type_id"])
#df.to_csv("csv/netflix_catalogo_drama.csv", index=False)