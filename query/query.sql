--essa query foi feita utilizando o ambiente do google bigquery 
-- ja tratei a unica coluna nula do dataset inteiro utilizando o COALESCE nativo do sql 

SELECT 
t1.*,
COALESCE(t1.OCCUPATION_TYPE, "not informed") AS OCCUPATION_TREATED,
t2.MONTHS_BALANCE,
t2.STATUS,
FROM jovial-duality-441115-b7.teste.application_record AS t1
JOIN jovial-duality-441115-b7.teste.credit_record AS t2
ON 
t1.ID = t2.ID