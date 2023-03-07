import pandas as pd
from validate_docbr import CPF, CNPJ
from sqlalchemy import create_engine

colnames = ['CPF', 'PRIVATE','INCOMPLETO','DATA_DA_ULTIMA_COMPRA','TICKET_MEDIO','TICKET_DA_ULTIMA_COMPRA', 'LOJA_MAIS_FREQUENTE', 'LOJA_DA_ULTIMA_COMPRA']
df_base_teste = pd.read_csv("base_teste[802].txt", skiprows=1, header=None, delim_whitespace=True,names=colnames)

cpf = CPF()
cnpj = CNPJ()

def valida_cpf(numero_cpf):
        return 'Válido' if cpf.validate(str(numero_cpf)) else 'Não válido'

def valida_cnpj(numero_cnpj):
        string_cnpj = str(numero_cnpj)
        if len(string_cnpj) == 18:
                return 'Válido' if cnpj.validate(string_cnpj) else 'Não válido'
        else:
                return 'Não informado'

df_base_teste['CPF_VALIDO'] = df_base_teste['CPF'].apply(valida_cpf)
df_base_teste['CNPJ_LOJA_MAIS_FREQUENTE_VALIDO'] = df_base_teste['LOJA_MAIS_FREQUENTE'].apply(valida_cnpj)
df_base_teste['CNPJ_LOJA_DA_ULTIMA_COMPRA_VALIDO'] = df_base_teste['LOJA_DA_ULTIMA_COMPRA'].apply(valida_cnpj)

connection_string = 'postgresql://neoway2023:neoway2023@host.docker.internal:5432/clients'

engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        connect_args={
                "connect_timeout": 40,
                "keepalives": 1,
                "keepalives_idle": 200,
                "keepalives_interval": 100,
                "keepalives_count": 15,
        }
    )
df_base_teste.to_sql(name='clients', schema='public', con=engine, if_exists='append', index=False)

print('Serviço executado com sucesso!')