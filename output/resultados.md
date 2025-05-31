# Documento de Análises de Dados

## 1. Análise de Outliers em Valor Total por Categoria

**Resumo da Metodologia:**
Utilizamos a análise de boxplot para identificar valores outliers entre as categorias de produtos. Isso envolveu calcular os quartis para cada categoria e identificar quaisquer valores que estão fora do intervalo interquartil (IQR).

**Resultado Encontrado:**
Categorias como "Beleza" e "Casa" apresentam outliers significativos, o que sugere que existem alguns pedidos com valores extremamente altos.

**Interpretação:**
A presença de outliers nas categorias "Beleza" e "Casa" pode indicar vendas extraordinárias ou erros de contabilização. Ajustes em estratégias de preço ou investigação de casos específicos podem ser necessários.

- **eixo_x**: `categoria`
- **eixo_y**: `valor_total`
- **tipo**: "Barra"

---

## 2. Avaliação de Desempenho de Canais de Origem

**Resumo da Metodologia:**
Soma dos valores totais das vendas agrupados por canal de origem para cada categoria de produto.

**Resultado Encontrado:**
O canal "Google Ads" gerou o maior valor de vendas em várias categorias, seguido por "Orgânico" e "Email".

**Interpretação:**
Os resultados sugerem que campanhas no Google Ads são altamente eficazes. Isso pode ser usado para alocar mais recursos para este canal.

- **eixo_x**: `canal_origem`
- **eixo_y**: `valor_total`
- **tipo**: "Barra"

---

## 3. Análise de Correlação entre Quantidade e Valor Total

**Resumo da Metodologia:**
Cálculo do coeficiente de correlação de Pearson entre as colunas `quantidade` e `valor_total`.

**Resultado Encontrado:**
Uma correlação positiva significativa foi encontrada, indicando que um aumento na quantidade de produtos comprados tende a aumentar o valor total do pedido.

**Interpretação:**
Isso suporta uma abordagem que foca em promoções que incentivem compras em maiores quantidades, pois pode resultar em vendas totais maiores.

- **eixo_x**: `quantidade`
- **eixo_y**: `valor_total`
- **tipo**: "Linha"

---

## 4. Análise Temporal de Compras Aprovadas

**Resumo da Metodologia:**
Distribuição das compras aprovadas ao longo do tempo para identificar tendências sazonais ou mensais. As datas de compras foram agrupadas por mês.

**Resultado Encontrado:**
Um aumento nos pedidos aprovados foi observado nos meses de março e abril.

**Interpretação:**
Podem existir sazonalidades ou campanhas específicas nestes meses que geram mais vendas aprovadas. Promoções podem ser planejadas para maximizar vendas durante esses períodos.

- **eixo_x**: `data_compra`
- **eixo_y**: `valor_total`
- **tipo**: "Linha"

---

## 5. Segmentação de Clientes por Categorias de Produtos

**Resumo da Metodologia:**
Segmentação de clientes com base nas categorias de produtos comprados usando frequências de compra.

**Resultado Encontrado:**
Clientes que compram "Eletrônicos" são mais propensos a fazer compras frequentemente, seguidos pelos que compram "Moda" e "Casa".

**Interpretação:**
Esses segmentos podem ser alvos de campanhas de marketing e ofertas personalizadas para aumentar ainda mais as vendas nas respectivas categorias.

- **eixo_x**: `cliente_id`
- **eixo_y**: `categoria`
- **tipo**: "Pizza"