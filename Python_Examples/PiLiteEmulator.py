V = [liczba głosów dla A,liczba głosów dla B,liczba głosów dla C]
s = [0,0,0]
 
for j in range(liczba mandatów):
    imax = 0
    for i in range(len(V)):
      if (V[i]/(2 * s[i] + 1)) > (V[imax]/(2 * s[imax] + 1)):
        imax = i
 
    s[imax] = s[imax] + 1
 
 
print s
