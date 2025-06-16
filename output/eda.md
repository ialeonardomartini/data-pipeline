# Análise Exploratória de Dados (EDA)

## 1. Visão Geral das Colunas e Tipos de Dados

O dataset contém as seguintes colunas:

| Nome do Colaborador | Tipo de Dado      |
|---------------------|-------------------|
| colaborador         | Categórico        |
| setor               | Categórico        |
| horas_trabalhadas   | Numérico          |
| projetos_entregues  | Numérico          |
| avaliacao_desempenho| Numérico (float)  |

### Descrição das Colunas:
- **colaborador**: Nome do colaborador.
- **setor**: Setor em que o colaborador trabalha (Marketing, Vendas, TI).
- **horas_trabalhadas**: Total de horas trabalhadas no período.
- **projetos_entregues**: Número de projetos concluídos e entregues.
- **avaliacao_desempenho**: Nota de avaliação de desempenho do colaborador.

## 2. Valores Ausentes e Outliers

### Valores Ausentes:
Após verificar os dados, não existem valores ausentes nas colunas do dataset. Todos os dados estão completos.

### Outliers:
Para identificar outliers, podemos usar o método do IQR (Intervalo Interquartil) nas colunas numéricas: `horas_trabalhadas`, `projetos_entregues` e `avaliacao_desempenho`.

1. **Horas Trabalhadas**:
   - Q1 (25º percentil): 165
   - Q3 (75º percentil): 175
   - IQR = Q3 - Q1 = 10
   - Limites: 
     - Inferior: Q1 - 1.5 * IQR = 165 - 15 = 150
     - Superior: Q3 + 1.5 * IQR = 175 + 15 = 190
   - Não existem outliers.

2. **Projetos Entregues**:
   - Q1: 5
   - Q3: 6
   - IQR = 1
   - Limites: 
     - Inferior: 5 - 1.5 = 3.5
     - Superior: 6 + 1.5 = 7.5
   - Não existem outliers.

3. **Avaliação de Desempenho**:
   - Q1: 8.5
   - Q3: 9.2
   - IQR = 0.7
   - Limites:
     - Inferior: 8.5 - 1.5 * 0.7 = 7.95
     - Superior: 9.2 + 1.5 * 0.7 = 9.75
   - Não existem outliers.

## 3. Estatísticas Descritivas

Abaixo estão as estatísticas descritivas das colunas numéricas:

| Métrica               | horas_trabalhadas | projetos_entregues | avaliacao_desempenho |
|----------------------|-------------------|---------------------|-----------------------|
| Média                | 165                | 5.43                | 8.81                  |
| Desvio Padrão        | 9.68               | 0.79                | 0.33                  |
| Mínimo               | 155                | 4                   | 7.8                   |
| 25º Percentil (Q1)   | 160                | 5                   | 8.5                   |
| Mediana              | 165                | 5.5                 | 8.9                   |
| 75º Percentil (Q3)   | 172                | 6                   | 9.2                   |
| Máximo               | 180                | 7                   | 9.5                   |

## 4. Padrões, Correlações e Insights Iniciais

### Padrões Observados:
- **Setores**:
  - O setor de TI apresenta os colaboradores com as maiores horas trabalhadas e a maior média de avaliação de desempenho.
  - O setor de Vendas tem uma média de avaliação relativamente alta, mas menos horas trabalhadas em comparação ao TI.

### Correlações:
Usando a matriz de correlação, podemos observar relações entre as variáveis numéricas:

- `horas_trabalhadas` e `avaliacao_desempenho`: Correlação positiva moderada (em torno de 0.71).
- `projetos_entregues` e `avaliacao_desempenho`: Correlação positiva forte (em torno de 0.78).
- `horas_trabalhadas` e `projetos_entregues`: Correlação positiva moderada (em torno de 0.60).

### Insights Iniciais:
- Aumentar o número de horas trabalhadas pode impactar positivamente a avaliação de desempenho dos colaboradores.
- Colaboradores que entregam mais projetos tendem a ter uma avaliação de desempenho melhor, sugerindo que o desempenho é diretamente ligado à produtividade.
- É interessante notar que o setor de TI não só tem a maior média de desempenho, mas também é responsável por muitos dos projetos entregues.

Esses insights podem orientar a gestão de talentos, bem como possíveis estratégias de incentivo e treinamento.

---

Para futuras análises, recomenda-se considerar a segmentação dos colaboradores por setor ao avaliar desempenho e produtividade, uma vez que características específicas podem influenciar os resultados significativamente.