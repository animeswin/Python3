produtos = {}

for i in range(5):
    nome = input(f"Insira o nome do produto {i + 1}: ")
    preco = float(input(f"Insira o preço do produto {i + 1}: "))
    produtos[nome] = preco

valor_total = sum(produtos.values())

print("\nProdutos e seus preços:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {valor_total:.2f}")