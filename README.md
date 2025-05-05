# 🧊 Code Freezing

**Code Freezing** é uma ferramenta para monitorar e aplicar períodos de congelamento de código (code freeze) em repositórios Git. Ela verifica o status de congelamento com base em uma configuração YAML e impede alterações em períodos críticos, como durante deploys ou homologações.

## 🚀 Funcionalidades

- Leitura de configurações de congelamento a partir de um arquivo `config.yml`.
- Verificação automática do status de congelamento com base na data e hora atuais.
- Integração com pipelines de CI/CD para bloquear execuções durante o freeze.
- Suporte a múltiplos ambientes e branches.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Dependências:** listadas em `requirements.txt`
- **Orquestração:** Docker Compose (opcional, conforme `docker-compose.yml`)

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GasparGui/code-freezing.git
   cd code-freezing
