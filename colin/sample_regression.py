# -*- coding: utf-8 -*-
# from sklearn import datasets
# import os
# import random
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# def read_data(file_path):
#     data = []
#     if os.path.isfile(file_path):
#         f = open(file_path, 'r')
#         samples = list(f.readlines())
#         f.close()
#         samples = [sample.strip() for sample in samples if len(sample.strip()) > 0]
#         for sample in samples:
#             sample_arr = sample.split('\t')
#             feature_arr = map(float, sample_arr[:-1])
#             label = int(float("{0:.2f}".format(float(sample_arr[-1]))))
#             data.append((feature_arr, label))
#     return data

# def read_feature_data(file_path):
#     data = []
#     if os.path.isfile(file_path):
#         f = open(file_path, 'r')
#         samples = list(f.readlines())
#         f.close()
#         samples = [sample.strip() for sample in samples if len(sample.strip()) > 0]
#         for sample in samples:
#             sample_arr = sample.split('\t')
#             feature_arr = map(float, sample_arr)
#             data.append(feature_arr)
#     return data
#
# print("Data length")
# feature_data = read_feature_data('/home/colin/projects/tech-ml/data/customer_salary_satisfaction')
#
# train_data = random.sample(feature_data, 800)
#
# test_data = [item for item in feature_data if item not in train_data]
#
# print(len(test_data))
#
# print(' ----- data -----')
# print(feature_data)


from utils import data_helpers
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt


def load_train_data(file_path='../data/customer_salary_satisfaction'):
    train_data = data_helpers.read_feature_data(file_path)
    feature_dim = len(train_data[0]) - 1
    feature_data = []
    target_data = []
    for data_sample in train_data:
        feature_vec = []
        for id_ in range(feature_dim):
            feature_vec.append(data_sample[id_])
        feature_data.append(feature_vec)
        target_data.append(data_sample[feature_dim])
    return feature_data, target_data


def train():
    x_data, y_data = load_train_data()
    x_train_data = x_data[:-200]
    y_train_data = y_data[:-200]
    lin_res = linear_model.LinearRegression()
    lin_res.fit(x_train_data, y_train_data)
    print('Coefficients:')
    print(lin_res.coef_)
    return lin_res


def test():
    x_data, y_data = load_train_data()
    x_test_data = x_data[-200:]
    y_test_data = y_data[-200:]
    lin_res = train()
    predict_y_data = lin_res.predict(x_test_data)
    # Mean square error
    mean_sq_err = np.mean((predict_y_data - y_test_data) ** 2)
    print('Mean square errors')
    print(mean_sq_err)
    variance_score = lin_res.score(x_test_data, y_test_data)
    print('Variance score (1.0 is perfect)')
    print(variance_score)
    # Plot data
    # Plot outputs
    plt.scatter(x_test_data, y_test_data,  color='black')
    plt.plot(x_test_data, predict_y_data, color='blue',
             linewidth=3)
    # plt.xticks(())
    # plt.yticks(())

    plt.show()

if __name__ == '__main__':
    # train()
    test()

print('feature data')
print(load_train_data(file_path='../data/customer_salary_satisfaction')[0])

print('target data')
print(load_train_data(file_path='../data/customer_salary_satisfaction')[1])