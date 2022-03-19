import numpy as np

def calculate(list):
    lista = list
    if len(lista) < 9:
      raise ValueError("List must contain nine numbers.")
         
    array = np.array([lista])
    arr = np.reshape(array, (3, 3))
    mean = [[arr[:, 0].mean(), arr[:, 1].mean(), arr[:, 2].mean()], [arr[0].mean(), arr[1].mean(), arr[2].mean()], arr.mean()]
    variance = [[arr[:, 0].var(), arr[:, 1].var(), arr[:, 2].var()], [arr[0].var(), arr[1].var(), arr[2].var()], arr.var()]
    sd_dv = [[np.std(arr[:, 0]), np.std(arr[:, 1]), np.std(arr[:, 2])], [np.std(arr[0]), np.std(arr[1]), np.std(arr[2])], np.std(arr)]
    maxim = [[arr[:, 0].max(), arr[:, 1].max(), arr[:, 2].max()], [arr[0].max(), arr[1].max(), arr[2].max()], arr.max()]
    minim = [[arr[:, 0].min(), arr[:, 1].min(), arr[:, 2].min()], [arr[0].min(), arr[1].min(), arr[2].min()], arr.min()]
    sumar = [[arr[:, 0].sum(), arr[:, 1].sum(), arr[:, 2].sum()], [arr[0].sum(), arr[1].sum(), arr[2].sum()], arr.sum()]
    calculations = {'mean': mean, 'variance': variance, 'standard deviation': sd_dv, 'max': maxim, 'min': minim, 'sum': sumar}




    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))