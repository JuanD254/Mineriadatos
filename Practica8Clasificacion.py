import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Clasificación de datos (Classification) KNN

df = pd.read_csv("csv/netflix_catalogo_drama.csv")
dat_knn = df.drop(columns=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','rating', 'duration', 'listed_in', 'description'])
X = dat_knn.iloc[:, [1,2]].values
y = dat_knn.iloc[:, [0]].values.ravel()

# Crear los datasets prueba y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Estandarizar escalas
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Crear el modelo de KNN
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)

# Hacer predicción
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Gráficos los resultados
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                    np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Prueba)')
plt.xlabel('País_Id')
plt.ylabel('Año')
plt.legend()
#plt.show()
#plt.savefig('img/plot_knn_datos.png')
plt.close()