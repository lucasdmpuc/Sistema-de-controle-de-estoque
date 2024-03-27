import tabulate as tabulate 
import pandas as pd 
from colorama import init, Fore, Back, Style

# todas as variaves do cadastro de produto
Cp = int(input("Informe o código do produto: "))
Np = str(input("Informe o nome do produto: "))
Dp = str(input("Informe a descrição do produto: "))
Ca = float(input("Informe o custo do produto: "))
Cf = float(input("Informe o custo fixo: "))
Cv = float(input("Informe o quanto sera a comissão de vendas: "))
Iv = float(input("Informe os impostos: "))
Ml = float(input("Informe a rentabilidade: "))



#calculo do preço de venda  
Pv = Ca/(1-((Cf+Cv+Iv+Ml)/(100)) )
print(f"{Pv}")
Rb = Pv - Ca

#Calculo das porcentagens para inserção na tabela
custoAq = Ca/Pv * 100
receitaBruta = 100- custoAq
impostos = (Iv/100) * Pv
comissãoVendas =(Cv/100) * Pv
rentabilidade = (Ml/100) * Pv
outrosCustos = Cf+Cv+Iv
outrosCustos1 = (Cf + Cv + Iv)/(100) * Pv 
custoFixo = (Cf/100) * Pv


#tabela 
tabela = {
    "Descrição": ["A-Preço de venda", "B-Custo de aquisação(fornecedor)", "C-Receita Bruta(A-B)","D-Custo fixo/administrativo","E-Comissão de vendas", "F-Impostos", "G-Rentabilidade", "F-Outros Custos"],
    "Valor": [Pv,Ca,Rb,custoFixo,comissãoVendas,impostos,rentabilidade,outrosCustos1],
    "%": ["100%", (f"{custoAq}%"), (f"{receitaBruta}%"),(f"{Cf}%"),(f"{Cv}%"), (f"{Iv}%"), (f"{Ml}%"), (f"{outrosCustos}%")]
}

print(tabulate.tabulate(tabela, headers='keys', tablefmt='fancy_grid'))

#analise de faixa de lucro 
if(Ml > 20):
 nomeTab = "O lucro sera Alto"
elif(Ml> 10 or Ml <= 20):
 nomeTab = "o lucro sera médio"
elif(Ml > 0 or Ml <= 10):
 nomeTab = "lucro sera baixo"
elif(Ml == 0):
 nome_na_tabela = "Não ira ter lucro nem prejuizo"
else :  
  nome_na_tabela = "Prejuizo"

#tabela mostrando o resultado obtido pela empresa  
lucro = Ml
tabLuc = {
 "Resultado": [f"{lucro}%", f"{nomeTab}"]
}
print(tabulate.tabulate(tabLuc, headers='keys', tablefmt="fancy_grid"))
