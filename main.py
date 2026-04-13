# main.py
from processador import media_idade, extremos_idade, contar_por_cidade

clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao.silva@email.com",
        "idade": 34, "cidade": "Joinville", "data_cadastro": "2023-01-10"},
    {"id": 2, "nome": "Maria Souza", "email": "maria@email",
        "idade": 28, "cidade": "Florianopolis", "data_cadastro": "2023-02-15"},
    {"id": 3, "nome": "Carlos Pereira", "email": "carlos.pereira@email.com",
        "idade": -5, "cidade": "Curitiba", "data_cadastro": "2023-03-20"},
    {"id": 4, "nome": "Ana Lima", "email": "ana.lima@email.com",
        "idade": 45, "cidade": "Joinville", "data_cadastro": "2023-01-25"},
    {"id": 5, "nome": "Pedro Santos", "email": "",
        "idade": 38, "cidade": "Sao Paulo", "data_cadastro": "2023-02-30"},
]

print(f"DataProcessor iniciado — {len(clientes)} clientes carregados.")

cidades = {}
for cliente in clientes:
            cidade = cliente["cidade"]
            cidade[cidade] = cidade.get(cidade, 0) + 1

for cidade, qtde in cidades.itens():
        pessoas = [cliente('nome') for cliente in clientes if cliente['cidade'] == cidade]
        print(f"(cidade)) ({qtde}): {','.join(pessoas)}")

media = media_idade(clientes)
minimo, maximo = extremos_idade(clientes)

print(f"Clientes carregados: {len(clientes)}")
print(f"Média de idade: {media:.1f}")
print(f"Faixa de idade: {minimo} – {maximo}")
print()
print("Clientes por cidade:")
for cidade, total in contar_por_cidade(clientes).items():
    print(f"  {cidade}: {total}")
