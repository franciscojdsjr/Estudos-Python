from tqdm import tqdm
import pandas as pd


#importando os arquivos
vendas_df = pd.read_csv(r'/home/francisco/Devlopment/Python Scripts/Hastag/Exercicios_Pandas/Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'/home/francisco/Devlopment/Python Scripts/Hastag/Exercicios_Pandas/Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'/home/francisco/Devlopment/Python Scripts/Hastag/Exercicios_Pandas/Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'/home/francisco/Devlopment/Python Scripts/Hastag/Exercicios_Pandas/Contoso - Clientes.csv', sep=';')

#limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})



pbar = tqdm(total = len(vendas_df['ID Loja']), position=0, leave=True)

for i, id_loja in enumerate(vendas_df['ID Loja']):
    if id_loja == 222:
        vendas_df.loc[i, 'Quantidade Devolvida'] += 1
    pbar.update()




    