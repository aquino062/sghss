# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde
## Documentação Completa do Projeto

---

## 📋 Índice
1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Modelagem](#modelagem)
4. [Implementação](#implementação)
5. [Plano de Testes](#plano-de-testes)
6. [Conclusão](#conclusão)
7. [Referências](#referências)

---

## 🏥 Introdução

### Sobre o Sistema
O **SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde)** é um sistema de gestão desenvolvido em Python com interface de terminal, projetado para auxiliar na administração de recursos hospitalares. O sistema oferece uma solução completa para gerenciamento de pacientes, profissionais de saúde, leitos e consultas médicas.

### Objetivos
- **Principal**: Desenvolver um sistema de gestão hospitalar funcional e intuitivo
- **Específicos**:
  - Gerenciar cadastro de pacientes com informações completas
  - Controlar profissionais de saúde e suas especialidades
  - Administrar leitos hospitalares e seus status
  - Agendar e gerenciar consultas médicas
  - Fornecer interface amigável com cores e ícones
  - Implementar validações de dados e tratamento de erros

### Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Banco de Dados**: SQLite3
- **Interface**: Terminal com cores ANSI
- **Sistema Operacional**: Windows/Linux/MacOS

---

## 📋 Requisitos

### Requisitos Funcionais (RF)

#### ✅ **RF01 - Gerenciamento de Pacientes**
- **Descrição**: Sistema deve permitir cadastro, edição, listagem e remoção de pacientes
- **Status**: ✅ **IMPLEMENTADO**
- **Funcionalidades**:
  - Cadastrar paciente com nome, CPF, data de nascimento, telefone e email
  - Validar CPF único
  - Editar informações do paciente
  - Listar todos os pacientes
  - Remover paciente do sistema

#### ✅ **RF02 - Gerenciamento de Profissionais**
- **Descrição**: Sistema deve permitir cadastro, edição, listagem e remoção de profissionais de saúde
- **Status**: ✅ **IMPLEMENTADO**
- **Funcionalidades**:
  - Cadastrar profissional com nome, cargo, registro e especialidade
  - Validar registro único
  - Editar informações do profissional
  - Listar todos os profissionais
  - Remover profissional do sistema

#### ✅ **RF03 - Gerenciamento de Leitos**
- **Descrição**: Sistema deve permitir cadastro, edição, listagem e remoção de leitos hospitalares
- **Status**: ✅ **IMPLEMENTADO**
- **Funcionalidades**:
  - Cadastrar leito com número, tipo e status
  - Validar número único
  - Editar informações do leito
  - Listar todos os leitos
  - Remover leito do sistema

#### ✅ **RF04 - Gerenciamento de Consultas**
- **Descrição**: Sistema deve permitir agendamento, edição, listagem e remoção de consultas
- **Status**: ✅ **IMPLEMENTADO**
- **Funcionalidades**:
  - Agendar consulta com paciente, profissional, data/hora e motivo
  - Validar relacionamentos entre paciente e profissional
  - Editar informações da consulta
  - Listar todas as consultas
  - Remover consulta do sistema

#### ✅ **RF05 - Interface de Usuário**
- **Descrição**: Sistema deve fornecer interface amigável e intuitiva
- **Status**: ✅ **IMPLEMENTADO**
- **Funcionalidades**:
  - Menu principal com navegação clara
  - Cores e ícones para melhor experiência
  - Mensagens de feedback (sucesso, erro, aviso)
  - Validação de entrada de dados

### Requisitos Não Funcionais (RNF)

#### ✅ **RNF01 - Performance**
- **Descrição**: Sistema deve responder rapidamente às operações
- **Status**: ✅ **IMPLEMENTADO**
- **Implementação**: Uso de SQLite3 para operações rápidas

#### ✅ **RNF02 - Usabilidade**
- **Descrição**: Interface deve ser intuitiva e fácil de usar
- **Status**: ✅ **IMPLEMENTADO**
- **Implementação**: Menu colorido com ícones e navegação clara

#### ✅ **RNF03 - Confiabilidade**
- **Descrição**: Sistema deve ser estável e confiável
- **Status**: ✅ **IMPLEMENTADO**
- **Implementação**: Tratamento de erros e validações

#### ✅ **RNF04 - Portabilidade**
- **Descrição**: Sistema deve funcionar em diferentes sistemas operacionais
- **Status**: ✅ **IMPLEMENTADO**
- **Implementação**: Python multiplataforma

#### ✅ **RNF05 - Manutenibilidade**
- **Descrição**: Código deve ser bem estruturado e documentado
- **Status**: ✅ **IMPLEMENTADO**
- **Implementação**: Código modular e comentado

---

## 🏗️ Modelagem

### Diagrama de Classes

```mermaid
classDiagram
    class Paciente {
        +Integer id
        +String nome
        +String cpf
        +String data_nascimento
        +String telefone
        +String email
    }
    
    class Profissional {
        +Integer id
        +String nome
        +String cargo
        +String registro
        +String especialidade
    }
    
    class Leito {
        +Integer id
        +String numero
        +String tipo
        +String status
    }
    
    class Consulta {
        +Integer id
        +Integer paciente_id
        +Integer profissional_id
        +String data_hora
        +String motivo
    }
    
    Consulta ||--o{ Paciente : "pertence a"
    Consulta ||--o{ Profissional : "realizada por"
```

### Casos de Uso

#### **UC01 - Gerenciar Pacientes**
- **Ator**: Administrador do Sistema
- **Pré-condições**: Sistema inicializado
- **Fluxo Principal**:
  1. Usuário seleciona "Gerenciar Pacientes"
  2. Sistema exibe menu de opções
  3. Usuário escolhe operação (adicionar, editar, listar, remover)
  4. Sistema executa operação solicitada
  5. Sistema exibe resultado da operação

#### **UC02 - Gerenciar Profissionais**
- **Ator**: Administrador do Sistema
- **Pré-condições**: Sistema inicializado
- **Fluxo Principal**:
  1. Usuário seleciona "Gerenciar Profissionais"
  2. Sistema exibe menu de opções
  3. Usuário escolhe operação (adicionar, editar, listar, remover)
  4. Sistema executa operação solicitada
  5. Sistema exibe resultado da operação

#### **UC03 - Gerenciar Leitos**
- **Ator**: Administrador do Sistema
- **Pré-condições**: Sistema inicializado
- **Fluxo Principal**:
  1. Usuário seleciona "Gerenciar Leitos"
  2. Sistema exibe menu de opções
  3. Usuário escolhe operação (adicionar, editar, listar, remover)
  4. Sistema executa operação solicitada
  5. Sistema exibe resultado da operação

#### **UC04 - Gerenciar Consultas**
- **Ator**: Administrador do Sistema
- **Pré-condições**: Sistema inicializado, pacientes e profissionais cadastrados
- **Fluxo Principal**:
  1. Usuário seleciona "Gerenciar Consultas"
  2. Sistema exibe menu de opções
  3. Usuário escolhe operação (adicionar, editar, listar, remover)
  4. Sistema executa operação solicitada
  5. Sistema exibe resultado da operação

### Modelo de Dados (DER)

```sql
-- Tabela de Pacientes
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento TEXT,
    telefone TEXT,
    email TEXT
);

-- Tabela de Profissionais
CREATE TABLE profissionais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    registro TEXT UNIQUE NOT NULL,
    especialidade TEXT
);

-- Tabela de Leitos
CREATE TABLE leitos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    status TEXT NOT NULL
);

-- Tabela de Consultas
CREATE TABLE consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    profissional_id INTEGER,
    data_hora TEXT,
    motivo TEXT,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY(profissional_id) REFERENCES profissionais(id)
);
```

---

## 💻 Implementação

### Estrutura do Projeto

```
VidaPlus_Willian II/
├── sghss_terminal.py          # Sistema principal
├── adicionar_dados.py         # Script para dados de exemplo
├── sghss_terminal.db          # Banco de dados SQLite
└── DOCUMENTACAO_SGHSS.md      # Esta documentação
```

### Principais Funcionalidades Implementadas

#### 1. Sistema de Cores e Interface
```python
class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    # ... mais cores
```

#### 2. Sistema de Ícones
```python
class Icones:
    HOSPITAL = "🏥"
    USER = "👤"
    DOCTOR = "👨‍⚕️"
    NURSE = "👩‍⚕️"
    BED = "🛏️"
    # ... mais ícones
```

#### 3. Conexão com Banco de Dados
```python
def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    conn = conectar()
    c = conn.cursor()
    # Criação das tabelas
    conn.commit()
    conn.close()
```

#### 4. Validações e Tratamento de Erros
```python
def print_sucesso(mensagem):
    print(f"\n{Cores.BRIGHT_GREEN}{Icones.SUCCESS} {mensagem}{Cores.RESET}")

def print_erro(mensagem):
    print(f"\n{Cores.BRIGHT_RED}{Icones.ERROR} {mensagem}{Cores.RESET}")
```

### Prints do Sistema em Execução

#### Menu Principal
```
======================================================================
🏥 SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde 🏥
======================================================================

╭─────────────────────────────────────╮
│ Menu Principal                      │
╰─────────────────────────────────────╯

  1 👤 Gerenciar Pacientes
  2 👨‍⚕️ Gerenciar Profissionais
  3 🛏️ Gerenciar Leitos
  4 📅 Gerenciar Consultas
  0 🚪 Sair do Sistema

──────────────────────────────────────────────────
Escolha uma opção:
```

#### Listagem de Pacientes
```
📋 LISTA DE PACIENTES
═══════════════════════════════════════════════════════════════

ID: 1 | Nome: Ana Silva Santos | CPF: 11111111111
Data Nascimento: 1990-01-15 | Telefone: 11999990001
Email: ana.silva@email.com

ID: 2 | Nome: Bruno Souza Costa | CPF: 22222222222
Data Nascimento: 1985-05-12 | Telefone: 11999990002
Email: bruno.souza@email.com

═══════════════════════════════════════════════════════════════
```

#### Adição de Paciente
```
➕ ADICIONAR NOVO PACIENTE
═══════════════════════════════════════════════════════════════

Nome completo: João Silva
CPF: 12345678901
Data de nascimento (YYYY-MM-DD): 1990-01-01
Telefone: 11999999999
Email: joao@email.com

✅ Paciente adicionado com sucesso!
```

### Link do GitHub
**Repositório**: [SGHSS - Sistema de Gestão Hospitalar](https://github.com/seu-usuario/sghss-sistema-gestao-hospitalar)

---

## 🧪 Plano de Testes

### Teste 1: Cadastro de Paciente
**Objetivo**: Verificar se o sistema aceita dados válidos de paciente

**Entrada**:
```
Nome: Maria Santos
CPF: 98765432100
Data Nascimento: 1985-06-15
Telefone: 11988887777
Email: maria@email.com
```

**Saída Esperada**:
```
✅ Paciente adicionado com sucesso!
```

**Resultado**: ✅ **PASSOU**

### Teste 2: Validação de CPF Duplicado
**Objetivo**: Verificar se o sistema rejeita CPF duplicado

**Entrada**:
```
CPF: 11111111111 (já cadastrado)
```

**Saída Esperada**:
```
❌ Erro: CPF já cadastrado no sistema!
```

**Resultado**: ✅ **PASSOU**

### Teste 3: Cadastro de Profissional
**Objetivo**: Verificar cadastro de profissional de saúde

**Entrada**:
```
Nome: Dr. Carlos Silva
Cargo: Médico
Registro: CRM54321
Especialidade: Cardiologia
```

**Saída Esperada**:
```
✅ Profissional adicionado com sucesso!
```

**Resultado**: ✅ **PASSOU**

### Teste 4: Cadastro de Leito
**Objetivo**: Verificar cadastro de leito hospitalar

**Entrada**:
```
Número: 105
Tipo: UTI
Status: Disponível
```

**Saída Esperada**:
```
✅ Leito adicionado com sucesso!
```

**Resultado**: ✅ **PASSOU**

### Teste 5: Agendamento de Consulta
**Objetivo**: Verificar agendamento de consulta

**Entrada**:
```
Paciente ID: 1
Profissional ID: 1
Data/Hora: 2024-02-15 14:00:00
Motivo: Consulta de rotina
```

**Saída Esperada**:
```
✅ Consulta agendada com sucesso!
```

**Resultado**: ✅ **PASSOU**

### Teste 6: Listagem de Dados
**Objetivo**: Verificar se as listagens funcionam corretamente

**Entrada**: Selecionar opção de listar

**Saída Esperada**: Tabela formatada com dados

**Resultado**: ✅ **PASSOU**

### Teste 7: Edição de Dados
**Objetivo**: Verificar se a edição funciona

**Entrada**: Selecionar editar e modificar dados

**Saída Esperada**:
```
✅ Dados atualizados com sucesso!
```

**Resultado**: ✅ **PASSOU**

### Teste 8: Remoção de Dados
**Objetivo**: Verificar se a remoção funciona

**Entrada**: Selecionar remover e confirmar

**Saída Esperada**:
```
✅ Registro removido com sucesso!
```

**Resultado**: ✅ **PASSOU**

---

## 🎯 Conclusão

### O que foi Implementado

O projeto **SGHSS** foi desenvolvido com sucesso, implementando todas as funcionalidades solicitadas:

✅ **Sistema completo de gestão hospitalar**
- Gerenciamento de pacientes
- Gerenciamento de profissionais
- Gerenciamento de leitos
- Gerenciamento de consultas

✅ **Interface amigável e intuitiva**
- Cores ANSI para melhor experiência visual
- Ícones Unicode para identificação rápida
- Menu navegável e responsivo
- Mensagens de feedback claras

✅ **Banco de dados robusto**
- SQLite3 para persistência de dados
- Relacionamentos entre tabelas
- Validações de integridade
- Script para dados de exemplo

✅ **Funcionalidades avançadas**
- Validação de dados de entrada
- Tratamento de erros
- Confirmações de operações críticas
- Estatísticas do sistema

### Aprendizados

1. **Desenvolvimento em Python**: Aprofundamento no uso de Python para desenvolvimento de sistemas
2. **Banco de Dados**: Experiência prática com SQLite3 e SQL
3. **Interface de Terminal**: Criação de interfaces amigáveis em terminal
4. **Validação de Dados**: Implementação de validações robustas
5. **Tratamento de Erros**: Boas práticas para tratamento de exceções
6. **Modularização**: Organização de código em funções e classes
7. **Documentação**: Importância da documentação completa

### Dificuldades Encontradas

1. **Compatibilidade de Cores**: Adaptação das cores ANSI para diferentes terminais
2. **Validação de CPF**: Implementação de validação robusta de CPF
3. **Relacionamentos**: Gerenciamento de chaves estrangeiras no SQLite
4. **Interface Responsiva**: Criação de interface que funcione bem em diferentes resoluções
5. **Tratamento de Entrada**: Validação e sanitização de dados de entrada

### Soluções Implementadas

1. **Cores ANSI**: Sistema de cores compatível com Windows e Unix
2. **Validação**: Sistema robusto de validação de dados
3. **Relacionamentos**: Uso de FOREIGN KEY constraints
4. **Interface**: Menu adaptativo com limpeza de tela
5. **Entrada**: Validação e tratamento de erros de entrada

### Melhorias Futuras

1. **Interface Gráfica**: Desenvolvimento de interface gráfica com tkinter ou PyQt
2. **Relatórios**: Sistema de geração de relatórios em PDF
3. **Backup**: Sistema automático de backup do banco de dados
4. **Usuários**: Sistema de autenticação e controle de acesso
5. **Logs**: Sistema de logs para auditoria
6. **API**: Desenvolvimento de API REST para integração

---

## 📚 Referências

### Documentação Oficial
- [Python Documentation](https://docs.python.org/3/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [ANSI Color Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

### Tutoriais e Guias
- [Python SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-python/)
- [Terminal Colors in Python](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)
- [Unicode Emoji List](https://unicode.org/emoji/charts/full-emoji-list.html)

### Frameworks e Bibliotecas
- **Python 3.x**: Linguagem principal do projeto
- **SQLite3**: Banco de dados embutido
- **OS**: Módulo para operações do sistema
- **Sys**: Módulo para funcionalidades do sistema
- **Time**: Módulo para operações de tempo
- **Datetime**: Módulo para manipulação de datas

### Ferramentas de Desenvolvimento
- **Visual Studio Code**: Editor de código
- **Git**: Controle de versão
- **GitHub**: Repositório remoto
- **Windows Terminal**: Terminal de desenvolvimento

### Sites de Referência
- [Stack Overflow](https://stackoverflow.com/) - Resolução de dúvidas técnicas
- [GitHub](https://github.com/) - Repositório e colaboração
- [Python.org](https://www.python.org/) - Recursos oficiais do Python
- [SQLite.org](https://www.sqlite.org/) - Recursos oficiais do SQLite

---

## 📄 Anexos

### Anexo A: Estrutura Completa do Banco de Dados
```sql
-- Script completo de criação das tabelas
-- Executado automaticamente pelo sistema

CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento TEXT,
    telefone TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS profissionais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    registro TEXT UNIQUE NOT NULL,
    especialidade TEXT
);

CREATE TABLE IF NOT EXISTS leitos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    profissional_id INTEGER,
    data_hora TEXT,
    motivo TEXT,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY(profissional_id) REFERENCES profissionais(id)
);
```

### Anexo B: Comandos de Execução
```bash
# Executar o sistema principal
python sghss_terminal.py

# Adicionar dados de exemplo
python adicionar_dados.py

# Verificar versão do Python
python --version
```

---

**Desenvolvido por**: Willian Aquino  
**Data**: 2024  
**Versão**: 1.0  
**Status**: ✅ Concluído 