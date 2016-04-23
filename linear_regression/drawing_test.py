# -*- coding: utf-8 -*-
from sklearn import datasets


def get_diabete_data():
    """
    Hầm được sử dụng để load dữ liệu diabete từ thư viện sklearn
    Sử dụng module datasets trong thư viện sklearn, hàm load_tên_bộ_dữ_liệu() được sử
    dụng để load bộ dữ liệu tương ứng. Dữ liệu trả về dưới dạng dictionary.
    Ta sử dụng key là 'data' để lấy ra dữ liệu dạng số.
    :return:
    """
    diabete_load = datasets.load_diabetes()
    return diabete_load['data']


if __name__ == '__main__':
    # Load dữ liệu từ sklearn sử dụng hàm đc định nghĩa phía trên
    diabete_data = get_diabete_data()
    # In ra số mẫu (sample) của bộ dữ liệu diabete
    print('Số lượng mẫu')
    print(len(diabete_data))
    print('Kích thước không gian feature')
    print(len(diabete_data[0]))
