


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
    mass = [5,10,2,8,11,0,12,17,22,28]
    SimpleSelectionSort(mass)