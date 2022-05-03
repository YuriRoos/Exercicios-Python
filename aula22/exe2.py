from operator import index

times='São Paulo','Santos','Red Bull Bragantino','Chapecoense','Juventude','América-MG','Athletico-PR','Atlético-GO','Atlético-MG','Avaí','Botafogo','Ceará','Corinthians','Coritiba','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Internacional'

a=(times[0:5])
print(f'os 5 primeiros times são: {a}')

b=(times[16:20])
print(f'os 4 ultimos times são: {b}')

c=sorted(times)
print(f'os times em ordem alfabetica são: {c}')

for index,nome in enumerate(times):
    if nome == 'Chapecoense':
        print(f'a Chapecoence apareceu na posiçao {index+1} posição.')






        