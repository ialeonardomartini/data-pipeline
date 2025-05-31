# Análise de Outliers do Valor Total

## Resumo da Metodologia
Utilizamos estatísticas descritivas para identificar outliers nas compras de diferentes categorias de produtos. Investigamos as causas das variações significativas no valor total das compras usando uma análise box-plot.

## Resultado Encontrado
Identificamos que a categoria "Moda" apresentou os maiores outliers no valor total das compras.

## Interpretação
Os outliers nessas categorias podem ser causados por itens de luxo ou produtos premium, além de descontos sazonais que resultam em compras de grandes volumes.

- **eixo_x**: categoria
- **eixo_y**: valor_total
- **tipo**: Barra

---

# Análise do Status de Pagamento Pendente

## Resumo da Metodologia
Filtramos transações com status de pagamento "Pendente" e analisamos as características dessas transações, como categoria do produto, canal de origem e data da compra.

## Resultado Encontrado
Transações pendentes são comumente associadas a compras de produtos eletrônicos e frequentemente realizadas via canais digitais, como Instagram e Google Ads.

## Interpretação
Podem haver questões técnicas na interface de pagamento desses canais, ou os produtos podem ter demanda alta levando a atrasos.

- **eixo_x**: categoria
- **eixo_y**: status_pagamento
- **tipo**: Barra

---

# Eficácia dos Canais de Marketing

## Resumo da Metodologia
Analisamos a correlação entre canais de marketing e o valor total das vendas através de uma análise gráfica para identificar quais canais trazem mais vendas.

## Resultado Encontrado
Canais como "Google Ads" e "Instagram" apresentaram uma correlação mais forte com altos valores de venda total.

## Interpretação
Investimentos nesses canais podem resultar em maior receita, sendo eficazes para a promoção de produtos com maior valor agregado.

- **eixo_x**: canal_origem
- **eixo_y**: valor_total
- **tipo**: Barra

---

# Análise de Tendências Temporais nas Compras

## Resumo da Metodologia
Utilizamos o método de série temporal para identificar padrões ou sazonalidades em compras mensais durante o ano de 2024.

## Resultado Encontrado
Observamos um aumento significativo em vendas nos meses de janeiro e fevereiro.

## Interpretação
O padrão pode estar relacionado a gastos de início de ano, como promoções de Ano Novo ou compras de recuperação de estoque após o período de festas.

- **eixo_x**: data_compra
- **eixo_y**: quantidade
- **tipo**: Linha

---

# Segmentação de Produtos e Clientes

## Resumo da Metodologia
Utilizamos técnicas de clusterização para agrupar clientes e produtos baseados nos seus padrões de compra, categorias e valores.

## Resultado Encontrado
Os clientes foram segmentados em grupos baseados na frequência de compra e nas categorias compradas, como produtos de Moda versus Eletrônicos.

## Interpretação
Essa segmentação permite ações de marketing mais direcionadas e personalização de ofertas com base nas preferências do cliente.

- **eixo_x**: cliente_id
- **eixo_y**: valor_total
- **tipo**: Pizza

---

Cada análise foi conduzida para fornecer insights práticos que podem orientar decisões de negócios futuras.