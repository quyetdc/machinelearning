from sklearn import datasets


def get_diabete_data():
    diabete_load = datasets.load_diabetes()
    return diabete_load['data']


if __name__ == '__main__':
    diabete_data = get_diabete_data()
    print(len(diabete_data))