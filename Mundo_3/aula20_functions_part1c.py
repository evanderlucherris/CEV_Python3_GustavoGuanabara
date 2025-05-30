def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
valores = [2, 5, 9, 7, 1, 4]
dobra(valores)
print(valores)