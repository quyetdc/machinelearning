import os
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def auto_gen_2d_regression_data(n=100, a=1.0, b=0.0, delta_b=0.05, x_range=[0.0, 1.0]):
    n = int(n)
    data = []
    if n > 0:
        for i in range(n):
            x_ = float(i) * (x_range[1] - x_range[0]) / n
            y_ = a * x_ + b + random.uniform(-1.0 * delta_b, delta_b)
            data.append([x_, y_])
    return data


def auto_gen_3d_regression_data(n=100, a=1.0, b=1.0, c=0.0, delta_c=0.05, x_range=[0.0, 1.0], y_range=[0.0, 1.0]):
    n = int(n)
    data = []
    if n > 0:
        for i in range(n):
            x_ = float(i) * (x_range[1] - x_range[0]) / n
            for j in range(n):
                y_ = float(j) * (y_range[1] - y_range[0]) / n
                z_ = a * x_ + b * y_ + random.uniform(-1.0 * delta_c, delta_c)
                data.append([x_, y_, z_])
    return data


def auto_gen_2d_classification_data(n=100, min_num=0.0, max_num=1.0):
    data = []
    avg_num = (min_num + max_num) / 2.0
    for id_ in range(n):
        ft1 = random.uniform(min_num, max_num)
        ft2 = random.uniform(min_num, max_num)
        if (ft1 < avg_num) & (ft2 < avg_num):
            label = 0
            data.append([ft1, ft2, label])
        elif (ft1 > avg_num) & (ft2 > avg_num):
            label = 1
            data.append([ft1, ft2, label])
    return data


def auto_gen_and_save_classification_data(n=100, file_path=''):
    if (n > 0) & (len(file_path) > 0):
        data = auto_gen_2d_classification_data(n=n)
        f = open(file_path, 'w')
        for sample_ in data:
            sample_str = map(str, sample_)
            f.write('\t'.join(sample_str))
            f.write('\n')
        f.close()


def auto_gen_and_save_regression_data(n=100, file_path='', feature_dim=2):
    if (n > 0) & (len(file_path) > 0):
        data = None
        if feature_dim == 2:
            data = auto_gen_2d_regression_data(n=n)
        if feature_dim == 3:
            data = auto_gen_3d_regression_data(n=n)
        if data is not None:
            f = open(file_path, 'w')
            for sample_ in data:
                sample_str = map(str, sample_)
                f.write('\t'.join(sample_str))
                f.write('\n')
            f.close()


def read_data(file_path):
    data = []
    if os.path.isfile(file_path):
        f = open(file_path, 'r')
        samples = list(f.readlines())
        f.close()
        samples = [sample.strip() for sample in samples if len(sample.strip()) > 0]
        for sample in samples:
            sample_arr = sample.split('\t')
            feature_arr = map(float, sample_arr[:-1])
            label = int(sample_arr[-1])
            data.append((feature_arr, label))
    return data


def read_feature_data(file_path):
    data = []
    if os.path.isfile(file_path):
        f = open(file_path, 'r')
        samples = list(f.readlines())
        f.close()
        samples = [sample.strip() for sample in samples if len(sample.strip()) > 0]
        for sample in samples:
            sample_arr = sample.split('\t')
            feature_arr = map(float, sample_arr)
            data.append(feature_arr)
    return data


def plot_data(file_path, plot_label=False):
    data = read_data(file_path)
    if len(data) > 0:
        xs = []
        ys = []
        labels = []
        for sample in data:
            feature_arr = sample[0]
            label = sample[1]
            xs.append(feature_arr[0])
            ys.append(feature_arr[1])
            labels.append(label)
        if plot_label:
            fig = plt.figure()

            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(xs, ys, labels, c='r', marker='o')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        else:
            plt.scatter(xs, ys, c='b', marker='o')

        plt.show()


def plot_regression_data(file_path):
    data = read_feature_data(file_path)
    if len(data) > 0:
        feature_size = len(data[0])
        xs = []
        ys = []
        zs = []
        for sample in data:
            xs.append(sample[0])
            if feature_size > 1:
                ys.append(sample[1])
            if feature_size > 2:
                zs.append(sample[2])
        if feature_size == 3:
            fig = plt.figure()

            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(xs, ys, zs, c='r', marker='o')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        elif feature_size == 2:
            plt.scatter(xs, ys, c='b', marker='o')
        else:
            plt.scatter(xs, c='b', marker='o')

        plt.show()


def main():
    print('starting...')
    # auto_gen_and_save_classification_data(n=1000, file_path='../data/customer_saving_salary')
    # plot_data(file_path='../data/customer_saving_salary')
    # auto_gen_and_save_regression_data(n=1000, file_path='../data/customer_salary_satisfaction')
    # plot_regression_data(file_path='../data/customer_salary_satisfaction')
    # auto_gen_and_save_regression_data(n=100, file_path='../data/customer_off_time_salary_satisfaction',
    #                                   feature_dim=3)
    plot_regression_data(file_path='../data/customer_off_time_salary_satisfaction')

if __name__ == '__main__':
    main()
