from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def kmeanClustering():
    irisData = datasets.load_iris()['data']

    # print('iris data:')
    # print(irisData)

    kmeanModel = KMeans(n_clusters=3)

    kmeanModel.fit(irisData)
    predict_labels = kmeanModel.predict(irisData)

    print('predict_labels: ')
    print(predict_labels)


    centroids = kmeanModel.cluster_centers_
    print('centroids:')
    print(centroids)

    xs0, ys0, zs0, xs1, ys1, zs1, xs2, ys2, zs2 = transfrom_data(irisData, predict_labels)

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs0, ys0, zs0, c='r', marker='o')
    ax.scatter(xs1, ys1, zs1, c='b', marker='o')
    ax.scatter(xs2, ys2, zs2, c='g', marker='o')

    plt.show()
    return True


# Input: rawData la iris data, array of 4-elements array
def transfrom_data(rawData, rawLabels):
    # length of each array element
    feature_dim = len(rawData[0]) - 1

    # divide data by label

    # ex1: label = 0
    xs0 = []
    ys0 = []
    zs0 = []

    xs1 = []
    ys1 = []
    zs1 = []

    xs2 = []
    ys2 = []
    zs2 = []

    for data_sample_id, data_sample in enumerate(rawData):
        if rawLabels[data_sample_id] == 0:
            xs0.append(data_sample[0])
            ys0.append(data_sample[1])
            zs0.append(data_sample[2])

        if rawLabels[data_sample_id] == 1:
            xs1.append(data_sample[0])
            ys1.append(data_sample[1])
            zs1.append(data_sample[2])

        if rawLabels[data_sample_id] == 2:
            xs2.append(data_sample[0])
            ys2.append(data_sample[1])
            zs2.append(data_sample[2])

    return xs0, ys0, zs0, xs1, ys1, zs1, xs2, ys2, zs2


kmeanClustering()