while True:
    tabuada=int(input("Tabuada do numero: "))

    for count in range(10):
        print("{} x {} = {}".format(tabuada, count+1, tabuada*(count+1)))
    
    if tabuada < 0:
        print('interrompido')
        break