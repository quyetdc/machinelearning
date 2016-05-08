from utils import data_helpers
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def load_train_data(file_path, label_pos=-1):
    train_data = data_helpers.read_feature_data(file_path)
    feature_dim = len(train_data[0]) - 1
    feature_data = []
    target_data = []
    if label_pos == 0:
        feature_ids = range(1, feature_dim + 1)
    else:
        feature_ids = range(feature_dim)
    for data_sample in train_data:
        feature_vec = []

        for id_ in feature_ids:
            feature_vec.append(data_sample[id_])
        feature_data.append(feature_vec)
        target_data.append(data_sample[label_pos])
    return feature_data, target_data


def plot_data(space_dim=2):
    feature_data, target_data = load_train_data(file_path='../data/customer_saving_salary')
    xs = np.array(feature_data)[:, 0]
    ys = np.array(feature_data)[:, 1]
    zs = target_data
    if space_dim == 2:
        plt.scatter(xs, ys, c='b', marker='o')
    elif space_dim == 3:
        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xs, zs, ys, c='r', marker='o')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
    plt.show()


def main():
    print('starting...')
    plot_data(space_dim=3)


if __name__ == '__main__':
    main()

