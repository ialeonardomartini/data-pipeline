# EDA CrewAI Pipeline

Pipeline de EDA (Exploratory Data Analysis) automatizado usando CrewAI Flows.

## 📋 Descrição

Este projeto implementa um pipeline automatizado de análise exploratória de dados utilizando múltiplas crews do CrewAI. O sistema é projetado para automatizar o processo de análise de dados, desde a definição das análises até a geração de insights e recomendações.

## 🚀 Funcionalidades

- **Definição Automática de Análises**: Utiliza IA para definir quais análises são mais relevantes para o conjunto de dados
- **Execução de Análises**: Realiza análises estatísticas e visuais de forma automatizada
- **Geração de Insights**: Extrai insights relevantes dos dados analisados
- **Recomendações**: Fornece recomendações baseadas nos insights obtidos
- **Pipeline Modular**: Arquitetura flexível que permite adicionar ou modificar análises facilmente

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- CrewAI
- Pydantic
- Python-dotenv
- PyYAML

## 📦 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd data-pipeline
```

2. Instale as dependências usando Poetry:
```bash
poetry install
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🎯 Uso

1. Ative o ambiente virtual:
```bash
poetry shell
```

2. Execute o pipeline:
```bash
poetry run start
```

## 📁 Estrutura do Projeto

```
data-pipeline/
├── src/
│   ├── crews/
│   │   ├── crew_define_analyses/
│   │   ├── crew_execute_analyses/
│   │   ├── crew_generate_insights/
│   │   └── crew_generate_recommendations/
│   ├── config/
│   └── run_pipeline.py
├── tests/
├── .env
├── .env.example
├── pyproject.toml
└── README.md
```

## 🔧 Configuração

O projeto utiliza arquivos YAML para configuração dos agentes e tarefas. Os arquivos de configuração estão localizados em:

- `src/crews/*/config/agents.yaml`: Configurações dos agentes
- `src/crews/*/config/tasks.yaml`: Configurações das tarefas

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Seu Nome - [email@example.com](mailto:email@example.com)

## 📞 Suporte

Para suporte, envie um email para [email@example.com](mailto:email@example.com) ou abra uma issue no repositório. 