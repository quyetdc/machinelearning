from sklearn import datasets

iris = datasets.load_iris().data
digits = datasets.load_digits().data
print(len(iris))
print(len(digits))