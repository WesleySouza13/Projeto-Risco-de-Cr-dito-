# Projeto Risco de Crédito 
# Contexto do problema

Bancos e empresas de aprovação de crédito enfrentam uma dificuldade em modelar com precisão quais clientes representam risco de inadimplencia. Essa limitação pode levar tanto à aprovação de crédito para clientes com alto risco, quanto à recusa de crédito para bons pagadores — impactando diretamente a rentabilidade e a confiança no sistema financeiro.

Este projeto tem como objetivo desenvolver um modelo preditivo de risco de crédito, utilizando técnicas de aprendizado de máquina para auxiliar instituições financeiras na tomada de decisão mais assertiva, justa e eficiente.

# Explicando as variáveis

ID -> Número ID do cliente	

CODE_GENDER	-> Gênero	

FLAG_OWN_CAR -> Tem um carro	

FLAG_OWN_REALTY	-> Existe uma propriedade	

CNT_CHILDREN -> Número de filhos

AMT_INCOME_TOTAL -> Renda anual	

NAME_INCOME_TYPE -> Categoria de renda	

NAME_EDUCATION_TYPE	-> Nível de escolaridade

NAME_FAMILY_STATUS -> Estado civil	

NAME_HOUSING_TYPE -> Modo de vida	

DAYS_BIRTH	-> Aniversário	Contagem regressiva a partir do dia atual (0), -1 significa ontem

DAYS_EMPLOYED ->Data de início do emprego	Contagem regressiva a partir do dia atual (0). Se positivo, significa que a pessoa está atualmente desempregada.

FLAG_MOBIL -> Existe um telefone celular? (1) para sim e (0) para não

FLAG_WORK_PHONE	-> Existe um telefone comercial? (1) para sim e (0) para não

FLAG_PHONE -> Tem algum telefone?	(1) para sim e (0) para não

FLAG_EMAIL -> Existe um e-mail	(1) para sim e (0) para não

OCCUPATION_TYPE	-> Ocupação	

CNT_FAM_MEMBERS	-> Tamanho da família

STATUS - 0: 1-29 dias de atraso 
1: 30-59 dias de atraso 
2: 60-89 dias de atraso 
3: 90-119 dias de atraso 
4: 120-149 dias de atraso 

MONTH_BALANCE -> Mes dos dados coletados
mês de registro: O mês dos dados extraídos é o ponto de partida, para trás, 0 é o mês atual
1: representa o mês anterior.

2: representa dois meses atrás.

3: três meses atrás...

E assim por diante.

# Análise descritiva e Univariada 

Nesta etapa, realizamos uma exploração inicial dos dados com foco em entender as características individuais de cada variável (análise univariada). O objetivo é identificar padrões, tendências, outliers e possíveis problemas nos dados, como valores ausentes ou distribuições assimétricas.
