```markdown
# Análise Exploratória de Dados (EDA)

## Introdução
Este relatório realiza uma Análise Exploratória de Dados (EDA) em um dataset de colaboradores e suas respectivas informações de setor, horas trabalhadas, projetos entregues e avaliação de desempenho. O objetivo é identificar padrões, correlações e insights iniciais.

## 1. Visão Geral das Colunas e Tipos de Dados
O dataset possui 5 colunas, conforme descrito abaixo:

- **colaborador**: Nome do colaborador (string)
- **setor**: Setor de trabalho (string)
- **horas_trabalhadas**: Quantidade de horas trabalhadas (inteiro)
- **projetos_entregues**: Número de projetos entregues (inteiro)
- **avaliacao_desempenho**: Avaliação de desempenho (float)

## 2. Valores Ausentes e Outliers
### Valores Ausentes
Não há valores ausentes no dataset, pois todas as colunas e linhas estão completas.

### Outliers
Uma análise visual rápida dos valores em cada coluna sugere que os valores estão em uma faixa razoável, dada a variabilidade esperada para cada métrica dentro do contexto corporativo. Contudo, uma análise mais aprofundada pode ser necessária usando técnicas estatísticas robustas caso o dataset expandisse.

## 3. Estatísticas Descritivas
Aqui estão as estatísticas descritivas das colunas numéricas:

- **Horas Trabalhadas**:
  - Média: 167.14
  - Mediana: 168
  - Mínimo: 155
  - Máximo: 180

- **Projetos Entregues**:
  - Média: 5.43
  - Mediana: 5
  - Mínimo: 4
  - Máximo: 7

- **Avaliação de Desempenho**:
  - Média: 8.97
  - Mediana: 9.1
  - Mínimo: 7.8
  - Máximo: 9.5

## 4. Padrões, Correlações e Insights Iniciais
### Padrões Observados
- **Setor de Trabalho**: O dataset contém colaboradores de três setores: Marketing, Vendas e TI.
  - Marketing: Alice, Carla
  - Vendas: Bruno, Fernanda
  - TI: Diego, Eduarda, Gustavo

- **Avaliação de Desempenho**: Os colaboradores da TI apresentam, em média, uma avaliação de desempenho mais alta em comparação com outros setores.

### Correlações
Baseando-se nas estatísticas descritivas e na inspeção visual:
- Existe uma tendência de colaboradores que trabalham mais horas [horas_trabalhadas] também entregarem mais projetos [projetos_entregues], especialmente observável em TI e Vendas.
- A avaliação de desempenho parece correlacionar-se positivamente, ainda que ligeiramente, com o número de horas trabalhadas e projetos entregues, sugerindo que maior produtividade pode estar associada a melhor desempenho.

### Insights Iniciais
- **Setor de TI**: Este setor possui as avaliações mais altas, possivelmente devido ao maior número de projetos ou horas trabalhadas, indicando uma alta produtividade que é reconhecida em avaliações.
- **Distribuição Justa**: Não há evidência clara de sobrecarga em termos de horas trabalhadas, pois os números permanecem em um intervalo esperado (entre 155 e 180 horas).

## Conclusão
Este EDA destaca que há variações entre setores em termos de produtividade e desempenho, com o setor de TI destacando-se em avaliações. A correlação positiva entre horas trabalhadas, projetos entregues e avaliação de desempenho sugere foco em produtividade e recompensas. Entretanto, para inferências gerais mais robustas, um dataset mais amplo seria benéfico.

```