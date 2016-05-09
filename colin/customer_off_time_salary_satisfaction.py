from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import os.path


def read_raw_data(file_path):
    raw_data = []
    if os.path.isfile(file_path): # check if file is existed
        f = open(file_path, 'r')
        raw_data = list(f.readlines())
        # we will have this ugly list
        # ['0.0\t0.0\t0.0172464689905\n', ...
        f.close()

        raw_data = [sample.strip() for sample in raw_data] # remove last '\n'

        # Split string '0.0\t0.0\t0.0172464689905' by '\t'
        # and map the result ( arr of three string number )=> arr of three float numbers
        raw_data = [map(float, sample.split('\t')) for sample in raw_data]

        # raw_data -> [[0.0, 0.0, 0.0172464689905], ...]

        return raw_data

print(' ---- raw data ---- ')

print(read_raw_data('../data/customer_off_time_salary_satisfaction'))

def load_train_data(file_path):
    raw_data = read_raw_data(file_path)
    feature_data = []
    target_data = []
    for data in raw_data:
        target_data.append(data[-1])
        feature_data.append(data[:-1])

    return feature_data, target_data


print
print(' ---- train data ---- ')
feature_data, target_data = load_train_data('../data/customer_off_time_salary_satisfaction')

print
print(' --------- feature data --------- ')
print(feature_data)

print
print(' --------- target data --------- ')
print(target_data)

def load_plot_data(file_path):
    raw_data = read_raw_data(file_path)
    x_data = []
    y_data = []
    z_data = []

    for data in raw_data:
        z_data.append(data[-1])
        x_data.append(data[:-1][0])
        y_data.append(data[:-1][1])

    return x_data, y_data, z_data

def train(file_path):
    feature_data, target_data = load_train_data(file_path)

    feature_train_data = feature_data[:-2000]
    target_train_data = target_data[:-2000]

    lin_res = linear_model.LinearRegression()
    lin_res.fit(feature_train_data, target_train_data)
    print('Coefficients:')
    print(lin_res.coef_)
    return lin_res

def test(file_path):
    feature_data, target_data = load_train_data(file_path)

    feature_test_data = feature_data[-2000:]
    target_test_data = target_data[-2000:]

    lin_res = train(file_path)
    predict_target_data = lin_res.predict(feature_test_data)
    mean_sq_err = np.mean((predict_target_data - target_test_data) ** 2)
    print('Mean square errors: ')
    print(mean_sq_err)

    explained_variance_score = lin_res.score(feature_test_data, target_test_data)
    print('Variance score (1.0 is the best)')
    print((explained_variance_score))

    x_1_data = np.array(feature_test_data)[:, 0]
    x_2_data = np.array(feature_test_data)[:, 1]
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_1_data, x_2_data, target_test_data, c='r', marker='o')
    # ax.plot(x_1_data, x_2_data, zs=target_test_data)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.scatter(x_1_data, x_2_data, predict_target_data, c='b', marker='D')

    plt.show()

print
print(' ------ Test ------ ')
test('../data/customer_off_time_salary_satisfaction')

