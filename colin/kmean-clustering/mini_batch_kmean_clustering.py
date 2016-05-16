from sklearn import datasets
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import os.path

def raw_unsupervised_data():
    raw_data = []
    if os.path.isfile('../../data/customer_data_min'):  # check if file is existed
        f = open('../../data/customer_data_min', 'r')
        raw_data = list(f.readlines())
        # we will have this ugly list
        # ['0.0\t0.0\t0.0172464689905\n', ...
        f.close()

        raw_data = [sample.strip() for sample in raw_data]  # remove last '\n'

        # Split string '0.0\t0.0\t0.0172464689905' by '\t'
        # and map the result ( arr of three string number )=> arr of three float numbers
        raw_data = [map(float, sample.split('\t')) for sample in raw_data]

        # raw_data -> [[0.0, 0.0, 0.0172464689905], ...]

    return raw_data

def miniBatchKmeanClustering():

    customer_data = raw_unsupervised_data()

    print('raw Data')
    print(customer_data)

    miniBatchKmeanModel = MiniBatchKMeans(n_clusters=3)

    miniBatchKmeanModel.fit(customer_data)
    predict_labels = miniBatchKmeanModel.predict(customer_data)

    print('predict_labels: ')
    print(predict_labels)

    centroids = miniBatchKmeanModel.cluster_centers_
    print('centroids:')
    print(centroids)

    xs0, ys0, zs0, xs1, ys1, zs1, xs2, ys2, zs2 = transfrom_data(customer_data, predict_labels)

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs0, ys0, zs0, c='r', marker='o')
    ax.scatter(xs1, ys1, zs1, c='b', marker='o')
    ax.scatter(xs2, ys2, zs2, c='g', marker='o')

    plt.show()
    return True

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


miniBatchKmeanClustering()