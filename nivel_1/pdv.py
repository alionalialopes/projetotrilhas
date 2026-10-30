#x=int(input("digite o nome de uma fruta: "))
#print(x+1)

compras=[]
nr_compras=0
total_bruto=0.0
total_desconto=0.0
total_final=0.0

while True:
    valor_compra=float(input("digite o valor da compra: "))
    if valor_compra==0:
        break
    
    idade=int(input("digite a idade: "))

    valor_desconto=valor_compra
    if idade >=65: 
        valor_desconto=valor_desconto*0.8

    if valor_desconto > 100:
        valor_desconto=valor_desconto*0.9

    print(f"R$ {valor_desconto}")
    compras.append({
        "valor_compra": valor_compra,
        "idade": idade,
        "valor_desconto": valor_desconto
    })
    nr_compras+=1
    total_bruto+=valor_compra
    total_desconto+=valor_compra-valor_desconto
    total_final+=valor_desconto

print("\nRESUMO FINAL")
print("------------------------------------")
print(f"Quantidade de compras: {nr_compras}")
print(f"Total bruto: R$ {total_bruto}")
print(f"Total de descontos concedidos: R$ {total_desconto}")
print(f"Total Final: R$ {total_final}")
print("------------------------------------")



    



#print("R$ "+str(valor_desconto))

#print(valor_compra)
#print(idade)
#print(valor_desconto)