def f(n,t,v,i):
    
    if i == len(n)-1:
        v_copia = v.copy()
        n_copia = [0]*len(n)
        for s in range(len(n)):
            n_copia[s] = int(n[s])

        x = 0
        while x < len(v_copia):
            if v_copia[x] == '*':
                n_copia[x] = n_copia[x] * n_copia[x+1]
                n_copia.pop(x+1)
                v_copia.pop(x)
                continue
            x += 1

        while len(n_copia) > 1:
            if v_copia[0] == '+':
                n_copia[0] = n_copia[0] + n_copia[1]
                n_copia.pop(1)
                v_copia.pop(0)
                continue
            n_copia[0] = n_copia[0] - n_copia[1]
            n_copia.pop(1)
            v_copia.pop(0)
            continue

        if n_copia[0] == t:
            mystring = n[0]
            for i in range(len(v)):
                mystring += v[i]
                mystring += n[i+1]
            print(mystring + " = " + str(t))
        
        return

    v[i] = '+'
    f(n,t,v,i+1)
    v[i] = '-'
    f(n,t,v,i+1)
    v[i] = '*'
    f(n,t,v,i+1)
    return

numbers = "123"
target = 6
operations = ['']*(len(numbers)-1)
index = 0
f(numbers, target, operations, index)

numbers = "232"
target = 8
operations = ['']*(len(numbers)-1)
index = 0
f(numbers, target, operations, index)