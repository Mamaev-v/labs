address = input('Введите адрес сети в формате х.х.х.х/х: ')
address = address.replace('/','.')
address = address.split('.')
oct1, oct2, oct3, oct4, mask = address

print(f'''
Network:
{oct1:<8} '''
      123