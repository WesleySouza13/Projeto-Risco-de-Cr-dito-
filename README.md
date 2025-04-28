# Projeto Risco de Crédito 
# Contexto do problema

Bancos e empresas de aprovação de crédito enfrentam uma dificuldade em modelar com precisão quais clientes representam risco de inadimplencia. Essa limitação pode levar tanto à aprovação de crédito para clientes com alto risco, quanto à recusa de crédito para bons pagadores impactando diretamente a rentabilidade e a confiança no sistema financeiro.

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

# Análise Bivariada 

Na parte de análise bivariada, busquei entender os comportamentos de clientes com base em seu gênero. Descobri fatores importantes que podem auxiliar na tomada de decisão, ou até entender a classificação do nosso modelo. Aqui vão as minhas descobertas:

1 - em sua maioria, o genero costuma possuir um carro, é o masculino.
2 - mulheres procuram possuir uma propriedade (casa, apartamento...) em seu nome.
3 - muitas mulheres não possuem filhos, isso é uma maioria entre as que possui 1 ou mais filhos. 
4 - homens costumam ter familias maiores em relação as mulheres. 
5 - as mulheres são maioria em empregabilidade ou em grupos de estudandes. 
6 - com a afirmação acima, as mulheres são maioria em questão de nivel de escolaridade em relação aos homens. 
7 - as mulheres são maioria em cargos de alto nivel, como staff de vendas, medicina etc. Por outro lado, também são uma maioria esmagadora entre os cargos não informados(ou desempregados). 

OBS: Com a analise de correlaçao, identifiquei que os dados nao possuem multicolinearidade. Com isso, temos dados praticamente ortogonais entre si, facilitando em uma possivel modelagem. 

# Análise de Cluster

Como os dados não possuíam rótulos definidos, foi necessário criar um agrupamento entre eles. Para isso, escolhi o algoritmo KMeans, que apresenta fácil implementação, boa visualização dos agrupamentos e dos centróides.

# Método do Cotovelo

Para definir de forma acertiva o número de clusters, utilizei o método do cotovelo.
Ele consiste em testar x vezes vários "range" do agrupamento até que possamos descobrir um número ótimo de clusters. O que acontece é que, conforme a quantidade de vezes que o número de clusters aumenta, também minimiza o erro. O detalhe está em identificar em qual ponto o erro começa a despencar.
No nosso caso, a divisão dos clusters ficou em k=2. 

Veja a imagem abaixo: 

![image](https://github.com/user-attachments/assets/451da0af-be4a-428f-8ad5-f4586fb44fcd)

# Silhouette Score

Para definir com maior precisão a quantidade de clusters a ser utilizada, realizei um teste utilizando o Silhouette Score, disponível em sklearn.metrics.silhouette_score. Com essa abordagem, foi possível identificar de forma mais clara o número ideal de clusters para o projeto.

![image](https://github.com/user-attachments/assets/10c66558-04d3-49a5-a0d3-6cff76bef863)

Vemos que realmente o número de clusters ideal é k = 2, pois é o ponto onde apresenta a maior pontuação.




