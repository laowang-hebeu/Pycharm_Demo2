import pickle


with open('sample_pickle.dat','rb') as f:
    n = pickle.load(f)
    for i in range(n):
        x = pickle.load(f)
        print(x)
