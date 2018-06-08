itensMochila = {'rope' : '1', 'torch' : '6', 'gold': '42', 'dagger' : '1', 'shield': '1'}
x = itensMochila.values()
x = list(x)


print('Inventário: ', '\nrope = ' + itensMochila['rope'], '\ntorch = '+ itensMochila['torch'], '\ngold = '+ itensMochila['gold'], '\ndagger = '+ itensMochila['dagger'], '\nshield = '+ itensMochila['shield'] )
print('Total:',int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4]),'ítens')

