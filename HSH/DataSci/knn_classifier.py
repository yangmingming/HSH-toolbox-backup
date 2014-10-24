##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-20

"""

"""

from __future__ import print_function
from sklearn.neighbors import DistanceMetric
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def dist(X, Y):
    """calculate X, Y distance matrix
    """
    distance_calculator = DistanceMetric.get_metric("euclidean")
    return distance_calculator.pairwise(X, Y)

def knn_find(train, test, k = 2):
    """find first K knn neighbors of test samples from train samples
    
    [Args]
    ----
    train: train data
        list of sample, each sample are list of features.
        e.g. [[age = 18, weight = 120, height = 167],
              [age = 45, weight = 180, height = 173],
              ..., ]
        
    test: test data
        data format is the same as train data
    
    k: number of neighbors
        how many neighbors you want to find
        
    [Returns]
    -------
    distances: list of distance of knn-neighbors from test data
        [[dist(test1, train_knn1), dist(test1, train_knn2), ...],
         [dist(test2, train_knn1), dist(test2, train_knn2), ...],
         ..., ]
    
    indices: list of indice of knn-neighbors from test data
        [[test1_train_knn1_index, test1_train_knn2_index, ...],
         [test2_train_knn1_index, test2_train_knn2_index, ...],
         ..., ]    
    """
    nbrs = NearestNeighbors(n_neighbors=k, algorithm="kd_tree").fit(train) # default = "kd_tree" algorithm
    return nbrs.kneighbors(test)

def prep_standardize(train, test, enable_verbose = False):
    """pre-processing, standardize data by eliminating mean and variance
    """
    scaler = preprocessing.StandardScaler().fit(train) # calculate mean and variance
    train = scaler.transform(train) # standardize train
    test = scaler.transform(test) # standardize test
    if enable_verbose:
        print("mean = %s" % scaler.mean_)
        print("var = %s" % scaler.std_)
    return train, test

def knn_classify(train, train_label, test, k=1, standardize=True):
    """classify test using KNN (k=1) algorithm
    
    usually the KNN classifier works good if all the features of the train
    data are continual value
    
    [Args]
    ------
    train: train data (see knn_find)
    
    train_label: train data's label
    
    test: test data
    
    k: knn classify value
    
    standardize: remove mean and variance or not
    
    [Returns]
    ---------
    test_label: test data's label
    
    [Notice]
    --------
        The sklearn.neighbors.KNeighborsClassifier doesn't do pre-processing
        this wrapper provide an option for that
    """
    if standardize:
        train, test = prep_standardize(train, test) # eliminate mean and variance
    neigh = KNeighborsClassifier(n_neighbors=k) # knn classifier
    neigh.fit(train, train_label) # training
    return neigh.predict(test) # classifying

if __name__ == "__main__":
    def dist_UT():
        train, test = ([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]], 
                       [[0,0], [1,1]])
        distances = dist(train, test)
        print("=== distance matrix ===\n%s\n" % distances)
        
    dist_UT()
    
    def knn_find_UT():
        train, test = ([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]], 
                       [[0,0], [1,1]])
        distances, indices = knn_find(train, test, 3)
        print("=== distance matrix ===\n%s\n" % distances)
        print("=== indices matrix ===\n%s\n" % indices)
        
    knn_find_UT()

    def knn_classify_UT():
        import pandas as pd
        train_data = pd.read_csv(r"demo_data\copd_1000.txt", header=None)
        train, train_label = train_data.loc[:, [0,2,3,4,5,6,7]], train_data.loc[:,8]
        test = [[81, 66, 8, 0.71, 0.67, 0.87, 1.61],
                [75, 53, 7, 0.95, 0.92, 0.98, 1.49]] ## there's no label
        test_label = knn_classify(train, train_label, test, k=1)
        print(test_label)
        
    knn_classify_UT()
        