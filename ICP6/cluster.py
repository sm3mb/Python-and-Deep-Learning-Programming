import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)

dataset = pd.read_csv('CC.csv')

#Handling NULL Values
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nulls.columns  = ['Null Count']
nulls.index.name  = 'Feature'

#Removing nulls
dataset['MINIMUM_PAYMENTS'].fillna(dataset['MINIMUM_PAYMENTS'].mean(), inplace=True)
dataset['CREDIT_LIMIT'].fillna(dataset['CREDIT_LIMIT'].mean(), inplace=True)
nullsnew = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nullsnew.columns  = ['Null Count']
nullsnew.index.name  = 'Feature'

x = dataset.iloc[:,1:-1]

#elbow method
wcss = []
for i in range(1,7):
    kmeans = KMeans(n_clusters=i,max_iter=300,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,7),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#building the model

km = KMeans(n_clusters=3)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans= km.predict(x)
from sklearn import metrics

# calculating the score
score = metrics.silhouette_score(x, y_cluster_kmeans)
print("score before scaling",score)

#scaling

scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)
x_scaler=scaler.transform(x)

#applying kmeans
nclusters = 3
seed = 0
km = KMeans(n_clusters=3)
km.fit(x_scaler)
y_cluster_kmeansscale = km.predict(x_scaler)

# calculating the score
scorenew = metrics.silhouette_score(x_scaler, y_cluster_kmeansscale)
print("score after scaling",scorenew)

# applying PCA

pca = PCA(2)
x_pca = pca.fit_transform(x)

#scaled data is x_scaler
#applying pca on x-scaler

pca = PCA(2)
x_pca_scaler = pca.fit_transform(x_scaler)


#PCA+KMEANS

##building the model
km = KMeans(n_clusters=3)
km.fit(x_pca)
# predict the cluster for each data point
y_cluster_kmeanspca= km.predict(x_pca)
from sklearn import metrics

pcameansscore = metrics.silhouette_score(x_pca, y_cluster_kmeanspca)
print("score after pca+kmeans",pcameansscore)

#2 SCALING+PCA+KMEANS

##building the model
km = KMeans(n_clusters=3)
km.fit(x_pca_scaler)
# predict the cluster for each data point
y_cluster_kmeansscaler= km.predict(x_pca_scaler)
from sklearn import metrics

pcascalmeascore = metrics.silhouette_score(x_pca_scaler, y_cluster_kmeansscaler)
print("score after scaling+pca+kmeans",pcascalmeascore)

# plot for SCALING+PCA+KMEANS
plt.scatter(x_pca_scaler[:, 0], x_pca_scaler[:, 1], c=y_cluster_kmeans, s=50, cmap='viridis')
plt.show()
