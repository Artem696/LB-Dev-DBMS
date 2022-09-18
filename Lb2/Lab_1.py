import numpy as np

def SimpleSelectionSort(mass):
    for i in range(len(mass)):
        min = mass[i]
        ixmin = i
        for j in range(i+1,len(mass)):
            if mass[j] < min:
                min = mass[j]
                ixmin = j
        mass[ixmin] = mass[i]
        mass[i] = min
    print(mass)




if __name__ == '__main__':
    mass = np.random.randint(0,100,20)
    print(mass)
    SimpleSelectionSort(mass)