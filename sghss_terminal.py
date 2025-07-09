import sqlite3
import os
import sys
import time
from datetime import datetime

# Cores ANSI expandidas para interface mais bonita
class Cores:
    # Cores básicas
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Cores de texto
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Cores de fundo
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Cores brilhantes
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Gradientes e efeitos especiais
    GRADIENT_BLUE = '\033[38;5;33m'
    GRADIENT_PURPLE = '\033[38;5;99m'
    GRADIENT_PINK = '\033[38;5;213m'
    GRADIENT_ORANGE = '\033[38;5;208m'
    GRADIENT_GREEN = '\033[38;5;46m'

# Ícones Unicode para interface
class Icones:
    HOSPITAL = "🏥"
    USER = "👤"
    DOCTOR = "👨‍⚕️"
    NURSE = "👩‍⚕️"
    BED = "🛏️"
    CALENDAR = "📅"
    PLUS = "➕"
    EDIT = "✏️"
    DELETE = "🗑️"
    LIST = "📋"
    BACK = "⬅️"
    EXIT = "🚪"
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"
    HEART = "❤️"
    PILL = "💊"
    SYRINGE = "💉"
    STETHOSCOPE = "🩺"

DB_NAME = 'sghss_terminal.db'

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        data_nascimento TEXT,
        telefone TEXT,
        email TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS profissionais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        registro TEXT UNIQUE NOT NULL,
        especialidade TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS leitos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero TEXT UNIQUE NOT NULL,
        tipo TEXT NOT NULL,
        status TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        profissional_id INTEGER,
        data_hora TEXT,
        motivo TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
        FOREIGN KEY(profissional_id) REFERENCES profissionais(id)
    )''')
    conn.commit()
    conn.close()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_carregamento(texto="Carregando", duracao=2):
    """Animação de carregamento bonita"""
    for i in range(duracao * 10):
        print(f"\r{Cores.BRIGHT_CYAN}{texto}{'.' * (i % 4)}{' ' * (3 - i % 4)}{Cores.RESET}", end='', flush=True)
        time.sleep(0.1)
    print()

def print_borda(texto, cor=Cores.BRIGHT_BLUE, largura=60):
    """Imprime texto com borda decorativa"""
    borda = "═" * (largura - 2)
    print(f"{cor}╔{borda}╗{Cores.RESET}")
    print(f"{cor}║{Cores.RESET}{texto.center(largura-2)}{cor}║{Cores.RESET}")
    print(f"{cor}╚{borda}╝{Cores.RESET}")

def print_titulo(texto):
    """Título principal com gradiente e ícones"""
    limpar_tela()
    print(f"\n{Cores.BRIGHT_CYAN}{'='*70}{Cores.RESET}")
    print(f"{Cores.GRADIENT_BLUE}{Cores.BOLD}{Icones.HOSPITAL} {texto} {Icones.HOSPITAL}{Cores.RESET}")
    print(f"{Cores.BRIGHT_CYAN}{'='*70}{Cores.RESET}\n")

def print_menu_titulo(texto):
    """Título de menu com estilo especial"""
    print(f"\n{Cores.BRIGHT_MAGENTA}{Cores.BOLD}╭{'─' * (len(texto) + 4)}╮{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}│ {Cores.BRIGHT_CYAN}{texto}{Cores.BRIGHT_MAGENTA} │{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}╰{'─' * (len(texto) + 4)}╯{Cores.RESET}\n")

def print_opcao_menu(numero, texto, icone=""):
    """Opção de menu com ícone e cores"""
    if numero == "0":
        cor = Cores.BRIGHT_RED
        icone = Icones.EXIT
    else:
        cor = Cores.BRIGHT_GREEN
    print(f"  {cor}{Cores.BOLD}{numero}{Cores.RESET} {icone} {texto}")

def print_sucesso(mensagem):
    """Mensagem de sucesso com ícone"""
    print(f"\n{Cores.BRIGHT_GREEN}{Icones.SUCCESS} {mensagem}{Cores.RESET}")

def print_erro(mensagem):
    """Mensagem de erro com ícone"""
    print(f"\n{Cores.BRIGHT_RED}{Icones.ERROR} {mensagem}{Cores.RESET}")

def print_aviso(mensagem):
    """Mensagem de aviso com ícone"""
    print(f"\n{Cores.BRIGHT_YELLOW}{Icones.WARNING} {mensagem}{Cores.RESET}")

def print_info(mensagem):
    """Mensagem informativa com ícone"""
    print(f"\n{Cores.BRIGHT_CYAN}{Icones.INFO} {mensagem}{Cores.RESET}")

def aguardar_enter():
    """Aguarda Enter com estilo"""
    input(f"\n{Cores.BRIGHT_BLUE}{Icones.INFO} Pressione Enter para continuar...{Cores.RESET}")

def menu_principal():
    while True:
        print_titulo('SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde')
        print_menu_titulo("Menu Principal")
        
        print_opcao_menu("1", "Gerenciar Pacientes", Icones.USER)
        print_opcao_menu("2", "Gerenciar Profissionais", Icones.DOCTOR)
        print_opcao_menu("3", "Gerenciar Leitos", Icones.BED)
        print_opcao_menu("4", "Gerenciar Consultas", Icones.CALENDAR)
        print_opcao_menu("0", "Sair do Sistema")
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            menu_pacientes()
        elif op == '2':
            menu_profissionais()
        elif op == '3':
            menu_leitos()
        elif op == '4':
            menu_consultas()
        elif op == '0':
            print(f"\n{Cores.BRIGHT_CYAN}{Icones.HEART} Obrigado por usar o SGHSS! {Icones.HEART}{Cores.RESET}")
            animacao_carregamento("Encerrando sistema", 1)
            sys.exit()
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

def menu_pacientes():
    while True:
        print_titulo('Gestão de Pacientes')
        print_menu_titulo("Menu de Pacientes")
        
        print_opcao_menu("1", "Listar Pacientes", Icones.LIST)
        print_opcao_menu("2", "Adicionar Paciente", Icones.PLUS)
        print_opcao_menu("3", "Editar Paciente", Icones.EDIT)
        print_opcao_menu("4", "Remover Paciente", Icones.DELETE)
        print_opcao_menu("0", "Voltar ao Menu Principal", Icones.BACK)
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            listar_pacientes()
        elif op == '2':
            adicionar_paciente()
        elif op == '3':
            editar_paciente()
        elif op == '4':
            remover_paciente()
        elif op == '0':
            break
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

def listar_pacientes():
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    pacientes = c.fetchall()
    
    print_titulo('Lista de Pacientes')
    
    if not pacientes:
        print_aviso("Nenhum paciente cadastrado no sistema.")
    else:
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}{'ID':<4} {'Nome':<25} {'CPF':<15} {'Nascimento':<12} {'Telefone':<15} {'Email':<20}{Cores.RESET}")
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        
        for p in pacientes:
            print(f"{Cores.BRIGHT_GREEN}{p[0]:<4}{Cores.RESET} {p[1]:<25} {p[2]:<15} {p[3]:<12} {p[4]:<15} {p[5]:<20}")
        
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}{Icones.SUCCESS} Total de pacientes: {len(pacientes)}{Cores.RESET}")
    
    conn.close()
    aguardar_enter()

def adicionar_paciente():
    print_titulo('Adicionar Novo Paciente')
    print_menu_titulo("Dados do Paciente")
    
    print(f"{Cores.BRIGHT_CYAN}Preencha os dados do paciente:{Cores.RESET}\n")
    
    nome = input(f"{Cores.BRIGHT_YELLOW}Nome completo: {Cores.RESET}")
    cpf = input(f"{Cores.BRIGHT_YELLOW}CPF: {Cores.RESET}")
    data_nascimento = input(f"{Cores.BRIGHT_YELLOW}Data de Nascimento (AAAA-MM-DD): {Cores.RESET}")
    telefone = input(f"{Cores.BRIGHT_YELLOW}Telefone: {Cores.RESET}")
    email = input(f"{Cores.BRIGHT_YELLOW}Email: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO pacientes (nome, cpf, data_nascimento, telefone, email) VALUES (?, ?, ?, ?, ?)',
                  (nome, cpf, data_nascimento, telefone, email))
        conn.commit()
        print_sucesso("Paciente cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("CPF já cadastrado no sistema!")
    conn.close()
    aguardar_enter()

def editar_paciente():
    listar_pacientes()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_paciente = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do paciente para editar: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes WHERE id=?', (id_paciente,))
    paciente = c.fetchone()
    
    if not paciente:
        print_erro("Paciente não encontrado!")
        conn.close()
        aguardar_enter()
        return
    
    print_titulo('Editar Paciente')
    print(f"{Cores.BRIGHT_GREEN}{Icones.USER} Editando paciente: {paciente[1]}{Cores.RESET}\n")
    
    nome = input(f"{Cores.BRIGHT_YELLOW}Novo nome [{paciente[1]}]: {Cores.RESET}") or paciente[1]
    cpf = input(f"{Cores.BRIGHT_YELLOW}Novo CPF [{paciente[2]}]: {Cores.RESET}") or paciente[2]
    data_nascimento = input(f"{Cores.BRIGHT_YELLOW}Nova data de nascimento [{paciente[3]}]: {Cores.RESET}") or paciente[3]
    telefone = input(f"{Cores.BRIGHT_YELLOW}Novo telefone [{paciente[4]}]: {Cores.RESET}") or paciente[4]
    email = input(f"{Cores.BRIGHT_YELLOW}Novo email [{paciente[5]}]: {Cores.RESET}") or paciente[5]
    
    try:
        c.execute('UPDATE pacientes SET nome=?, cpf=?, data_nascimento=?, telefone=?, email=? WHERE id=?',
                  (nome, cpf, data_nascimento, telefone, email, id_paciente))
        conn.commit()
        print_sucesso("Paciente atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("CPF já cadastrado para outro paciente!")
    
    conn.close()
    aguardar_enter()

def remover_paciente():
    listar_pacientes()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_paciente = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do paciente para remover: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes WHERE id=?', (id_paciente,))
    paciente = c.fetchone()
    
    if not paciente:
        print_erro("Paciente não encontrado!")
    else:
        confirmacao = input(f"{Cores.BRIGHT_RED}Tem certeza que deseja remover {paciente[1]}? (s/n): {Cores.RESET}").lower()
        if confirmacao == 's':
            c.execute('DELETE FROM pacientes WHERE id=?', (id_paciente,))
            conn.commit()
            print_sucesso("Paciente removido com sucesso!")
        else:
            print_info("Operação cancelada.")
    
    conn.close()
    aguardar_enter()

def menu_profissionais():
    while True:
        print_titulo('Gestão de Profissionais')
        print_menu_titulo("Menu de Profissionais")
        
        print_opcao_menu("1", "Listar Profissionais", Icones.LIST)
        print_opcao_menu("2", "Adicionar Profissional", Icones.PLUS)
        print_opcao_menu("3", "Editar Profissional", Icones.EDIT)
        print_opcao_menu("4", "Remover Profissional", Icones.DELETE)
        print_opcao_menu("0", "Voltar ao Menu Principal", Icones.BACK)
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            listar_profissionais()
        elif op == '2':
            adicionar_profissional()
        elif op == '3':
            editar_profissional()
        elif op == '4':
            remover_profissional()
        elif op == '0':
            break
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

def listar_profissionais():
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM profissionais')
    profissionais = c.fetchall()
    
    print_titulo('Lista de Profissionais')
    
    if not profissionais:
        print_aviso("Nenhum profissional cadastrado no sistema.")
    else:
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}{'ID':<4} {'Nome':<25} {'Cargo':<15} {'Registro':<12} {'Especialidade':<20}{Cores.RESET}")
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        
        for p in profissionais:
            icone = Icones.DOCTOR if p[2].lower() in ['médico', 'doctor', 'medico'] else Icones.NURSE
            print(f"{Cores.BRIGHT_GREEN}{p[0]:<4}{Cores.RESET} {icone} {p[1]:<23} {p[2]:<15} {p[3]:<12} {p[4]:<20}")
        
        print(f"{Cores.BRIGHT_CYAN}{'─'*80}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}{Icones.SUCCESS} Total de profissionais: {len(profissionais)}{Cores.RESET}")
    
    conn.close()
    aguardar_enter()

def adicionar_profissional():
    print_titulo('Adicionar Novo Profissional')
    print_menu_titulo("Dados do Profissional")
    
    print(f"{Cores.BRIGHT_CYAN}Preencha os dados do profissional:{Cores.RESET}\n")
    
    nome = input(f"{Cores.BRIGHT_YELLOW}Nome completo: {Cores.RESET}")
    cargo = input(f"{Cores.BRIGHT_YELLOW}Cargo: {Cores.RESET}")
    registro = input(f"{Cores.BRIGHT_YELLOW}Número de registro: {Cores.RESET}")
    especialidade = input(f"{Cores.BRIGHT_YELLOW}Especialidade: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO profissionais (nome, cargo, registro, especialidade) VALUES (?, ?, ?, ?)',
                  (nome, cargo, registro, especialidade))
        conn.commit()
        print_sucesso("Profissional cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Registro já cadastrado no sistema!")
    conn.close()
    aguardar_enter()

def editar_profissional():
    listar_profissionais()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_profissional = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do profissional para editar: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM profissionais WHERE id=?', (id_profissional,))
    profissional = c.fetchone()
    
    if not profissional:
        print_erro("Profissional não encontrado!")
        conn.close()
        aguardar_enter()
        return
    
    print_titulo('Editar Profissional')
    print(f"{Cores.BRIGHT_GREEN}{Icones.DOCTOR} Editando profissional: {profissional[1]}{Cores.RESET}\n")
    
    nome = input(f"{Cores.BRIGHT_YELLOW}Novo nome [{profissional[1]}]: {Cores.RESET}") or profissional[1]
    cargo = input(f"{Cores.BRIGHT_YELLOW}Novo cargo [{profissional[2]}]: {Cores.RESET}") or profissional[2]
    registro = input(f"{Cores.BRIGHT_YELLOW}Novo registro [{profissional[3]}]: {Cores.RESET}") or profissional[3]
    especialidade = input(f"{Cores.BRIGHT_YELLOW}Nova especialidade [{profissional[4]}]: {Cores.RESET}") or profissional[4]
    
    try:
        c.execute('UPDATE profissionais SET nome=?, cargo=?, registro=?, especialidade=? WHERE id=?',
                  (nome, cargo, registro, especialidade, id_profissional))
        conn.commit()
        print_sucesso("Profissional atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Registro já cadastrado para outro profissional!")
    
    conn.close()
    aguardar_enter()

def remover_profissional():
    listar_profissionais()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_profissional = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do profissional para remover: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM profissionais WHERE id=?', (id_profissional,))
    profissional = c.fetchone()
    
    if not profissional:
        print_erro("Profissional não encontrado!")
    else:
        confirmacao = input(f"{Cores.BRIGHT_RED}Tem certeza que deseja remover {profissional[1]}? (s/n): {Cores.RESET}").lower()
        if confirmacao == 's':
            c.execute('DELETE FROM profissionais WHERE id=?', (id_profissional,))
            conn.commit()
            print_sucesso("Profissional removido com sucesso!")
        else:
            print_info("Operação cancelada.")
    
    conn.close()
    aguardar_enter()

def menu_leitos():
    while True:
        print_titulo('Gestão de Leitos')
        print_menu_titulo("Menu de Leitos")
        
        print_opcao_menu("1", "Listar Leitos", Icones.LIST)
        print_opcao_menu("2", "Adicionar Leito", Icones.PLUS)
        print_opcao_menu("3", "Editar Leito", Icones.EDIT)
        print_opcao_menu("4", "Remover Leito", Icones.DELETE)
        print_opcao_menu("0", "Voltar ao Menu Principal", Icones.BACK)
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            listar_leitos()
        elif op == '2':
            adicionar_leito()
        elif op == '3':
            editar_leito()
        elif op == '4':
            remover_leito()
        elif op == '0':
            break
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

def listar_leitos():
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM leitos')
    leitos = c.fetchall()
    
    print_titulo('Lista de Leitos')
    
    if not leitos:
        print_aviso("Nenhum leito cadastrado no sistema.")
    else:
        print(f"{Cores.BRIGHT_CYAN}{'─'*60}{Cores.RESET}")
        print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}{'ID':<4} {'Número':<10} {'Tipo':<15} {'Status':<15}{Cores.RESET}")
        print(f"{Cores.BRIGHT_CYAN}{'─'*60}{Cores.RESET}")
        
        for l in leitos:
            status_cor = Cores.BRIGHT_GREEN if l[3].lower() == 'livre' else Cores.BRIGHT_RED
            print(f"{Cores.BRIGHT_GREEN}{l[0]:<4}{Cores.RESET} {Icones.BED} {l[1]:<8} {l[2]:<15} {status_cor}{l[3]:<15}{Cores.RESET}")
        
        print(f"{Cores.BRIGHT_CYAN}{'─'*60}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}{Icones.SUCCESS} Total de leitos: {len(leitos)}{Cores.RESET}")
    
    conn.close()
    aguardar_enter()

def adicionar_leito():
    print_titulo('Adicionar Novo Leito')
    print_menu_titulo("Dados do Leito")
    
    print(f"{Cores.BRIGHT_CYAN}Preencha os dados do leito:{Cores.RESET}\n")
    
    numero = input(f"{Cores.BRIGHT_YELLOW}Número do leito: {Cores.RESET}")
    tipo = input(f"{Cores.BRIGHT_YELLOW}Tipo (UTI/Enfermaria/Isolamento): {Cores.RESET}")
    status = input(f"{Cores.BRIGHT_YELLOW}Status (Livre/Ocupado): {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO leitos (numero, tipo, status) VALUES (?, ?, ?)',
                  (numero, tipo, status))
        conn.commit()
        print_sucesso("Leito cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Número de leito já cadastrado no sistema!")
    conn.close()
    aguardar_enter()

def editar_leito():
    listar_leitos()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_leito = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do leito para editar: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM leitos WHERE id=?', (id_leito,))
    leito = c.fetchone()
    
    if not leito:
        print_erro("Leito não encontrado!")
        conn.close()
        aguardar_enter()
        return
    
    print_titulo('Editar Leito')
    print(f"{Cores.BRIGHT_GREEN}{Icones.BED} Editando leito: {leito[1]}{Cores.RESET}\n")
    
    numero = input(f"{Cores.BRIGHT_YELLOW}Novo número [{leito[1]}]: {Cores.RESET}") or leito[1]
    tipo = input(f"{Cores.BRIGHT_YELLOW}Novo tipo [{leito[2]}]: {Cores.RESET}") or leito[2]
    status = input(f"{Cores.BRIGHT_YELLOW}Novo status [{leito[3]}]: {Cores.RESET}") or leito[3]
    
    try:
        c.execute('UPDATE leitos SET numero=?, tipo=?, status=? WHERE id=?',
                  (numero, tipo, status, id_leito))
        conn.commit()
        print_sucesso("Leito atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Número de leito já cadastrado para outro leito!")
    
    conn.close()
    aguardar_enter()

def remover_leito():
    listar_leitos()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_leito = input(f"{Cores.BRIGHT_YELLOW}Digite o ID do leito para remover: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM leitos WHERE id=?', (id_leito,))
    leito = c.fetchone()
    
    if not leito:
        print_erro("Leito não encontrado!")
    else:
        confirmacao = input(f"{Cores.BRIGHT_RED}Tem certeza que deseja remover o leito {leito[1]}? (s/n): {Cores.RESET}").lower()
        if confirmacao == 's':
            c.execute('DELETE FROM leitos WHERE id=?', (id_leito,))
            conn.commit()
            print_sucesso("Leito removido com sucesso!")
        else:
            print_info("Operação cancelada.")
    
    conn.close()
    aguardar_enter()

def menu_consultas():
    while True:
        print_titulo('Gestão de Consultas')
        print_menu_titulo("Menu de Consultas")
        
        print_opcao_menu("1", "Listar Consultas", Icones.LIST)
        print_opcao_menu("2", "Adicionar Consulta", Icones.PLUS)
        print_opcao_menu("3", "Editar Consulta", Icones.EDIT)
        print_opcao_menu("4", "Remover Consulta", Icones.DELETE)
        print_opcao_menu("0", "Voltar ao Menu Principal", Icones.BACK)
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            listar_consultas()
        elif op == '2':
            adicionar_consulta()
        elif op == '3':
            editar_consulta()
        elif op == '4':
            remover_consulta()
        elif op == '0':
            break
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

def listar_consultas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''SELECT c.id, p.nome as paciente, pr.nome as profissional, 
                  c.data_hora, c.motivo 
                  FROM consultas c 
                  JOIN pacientes p ON c.paciente_id = p.id 
                  JOIN profissionais pr ON c.profissional_id = pr.id''')
    consultas = c.fetchall()
    
    print_titulo('Lista de Consultas')
    
    if not consultas:
        print_aviso("Nenhuma consulta cadastrada no sistema.")
    else:
        print(f"{Cores.BRIGHT_CYAN}{'─'*100}{Cores.RESET}")
        print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}{'ID':<4} {'Paciente':<20} {'Profissional':<20} {'Data/Hora':<20} {'Motivo':<30}{Cores.RESET}")
        print(f"{Cores.BRIGHT_CYAN}{'─'*100}{Cores.RESET}")
        
        for c in consultas:
            print(f"{Cores.BRIGHT_GREEN}{c[0]:<4}{Cores.RESET} {Icones.USER} {c[1]:<18} {Icones.DOCTOR} {c[2]:<18} {c[3]:<20} {c[4]:<30}")
        
        print(f"{Cores.BRIGHT_CYAN}{'─'*100}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}{Icones.SUCCESS} Total de consultas: {len(consultas)}{Cores.RESET}")
    
    conn.close()
    aguardar_enter()

def adicionar_consulta():
    print_titulo('Adicionar Nova Consulta')
    print_menu_titulo("Dados da Consulta")
    
    # Listar pacientes disponíveis
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT id, nome FROM pacientes')
    pacientes = c.fetchall()
    
    if not pacientes:
        print_erro("Não há pacientes cadastrados para agendar consulta!")
        conn.close()
        aguardar_enter()
        return
    
    print(f"{Cores.BRIGHT_CYAN}Pacientes disponíveis:{Cores.RESET}")
    for p in pacientes:
        print(f"  {Cores.BRIGHT_GREEN}{p[0]}{Cores.RESET} - {p[1]}")
    
    # Listar profissionais disponíveis
    c.execute('SELECT id, nome, cargo FROM profissionais')
    profissionais = c.fetchall()
    
    if not profissionais:
        print_erro("Não há profissionais cadastrados para agendar consulta!")
        conn.close()
        aguardar_enter()
        return
    
    print(f"\n{Cores.BRIGHT_CYAN}Profissionais disponíveis:{Cores.RESET}")
    for p in profissionais:
        print(f"  {Cores.BRIGHT_GREEN}{p[0]}{Cores.RESET} - {p[1]} ({p[2]})")
    
    print(f"\n{Cores.BRIGHT_CYAN}Preencha os dados da consulta:{Cores.RESET}\n")
    
    paciente_id = input(f"{Cores.BRIGHT_YELLOW}ID do paciente: {Cores.RESET}")
    profissional_id = input(f"{Cores.BRIGHT_YELLOW}ID do profissional: {Cores.RESET}")
    data_hora = input(f"{Cores.BRIGHT_YELLOW}Data e hora (AAAA-MM-DD HH:MM): {Cores.RESET}")
    motivo = input(f"{Cores.BRIGHT_YELLOW}Motivo da consulta: {Cores.RESET}")
    
    try:
        c.execute('INSERT INTO consultas (paciente_id, profissional_id, data_hora, motivo) VALUES (?, ?, ?, ?)',
                  (paciente_id, profissional_id, data_hora, motivo))
        conn.commit()
        print_sucesso("Consulta agendada com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Erro ao agendar consulta. Verifique os IDs informados.")
    
    conn.close()
    aguardar_enter()

def editar_consulta():
    listar_consultas()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_consulta = input(f"{Cores.BRIGHT_YELLOW}Digite o ID da consulta para editar: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM consultas WHERE id=?', (id_consulta,))
    consulta = c.fetchone()
    
    if not consulta:
        print_erro("Consulta não encontrada!")
        conn.close()
        aguardar_enter()
        return
    
    print_titulo('Editar Consulta')
    print(f"{Cores.BRIGHT_GREEN}{Icones.CALENDAR} Editando consulta ID: {consulta[0]}{Cores.RESET}\n")
    
    # Buscar dados relacionados
    c.execute('SELECT nome FROM pacientes WHERE id=?', (consulta[1],))
    paciente_nome = c.fetchone()[0]
    c.execute('SELECT nome FROM profissionais WHERE id=?', (consulta[2],))
    profissional_nome = c.fetchone()[0]
    
    print(f"{Cores.BRIGHT_CYAN}Paciente atual: {paciente_nome}{Cores.RESET}")
    print(f"{Cores.BRIGHT_CYAN}Profissional atual: {profissional_nome}{Cores.RESET}\n")
    
    # Listar opções para seleção
    c.execute('SELECT id, nome FROM pacientes')
    pacientes = c.fetchall()
    print(f"{Cores.BRIGHT_CYAN}Pacientes disponíveis:{Cores.RESET}")
    for p in pacientes:
        print(f"  {Cores.BRIGHT_GREEN}{p[0]}{Cores.RESET} - {p[1]}")
    
    c.execute('SELECT id, nome FROM profissionais')
    profissionais = c.fetchall()
    print(f"\n{Cores.BRIGHT_CYAN}Profissionais disponíveis:{Cores.RESET}")
    for p in profissionais:
        print(f"  {Cores.BRIGHT_GREEN}{p[0]}{Cores.RESET} - {p[1]}")
    
    print(f"\n{Cores.BRIGHT_CYAN}Novos dados da consulta:{Cores.RESET}\n")
    
    paciente_id = input(f"{Cores.BRIGHT_YELLOW}Novo ID do paciente [{consulta[1]}]: {Cores.RESET}") or consulta[1]
    profissional_id = input(f"{Cores.BRIGHT_YELLOW}Novo ID do profissional [{consulta[2]}]: {Cores.RESET}") or consulta[2]
    data_hora = input(f"{Cores.BRIGHT_YELLOW}Nova data e hora [{consulta[3]}]: {Cores.RESET}") or consulta[3]
    motivo = input(f"{Cores.BRIGHT_YELLOW}Novo motivo [{consulta[4]}]: {Cores.RESET}") or consulta[4]
    
    try:
        c.execute('UPDATE consultas SET paciente_id=?, profissional_id=?, data_hora=?, motivo=? WHERE id=?',
                  (paciente_id, profissional_id, data_hora, motivo, id_consulta))
        conn.commit()
        print_sucesso("Consulta atualizada com sucesso!")
    except sqlite3.IntegrityError:
        print_erro("Erro ao atualizar consulta. Verifique os IDs informados.")
    
    conn.close()
    aguardar_enter()

def remover_consulta():
    listar_consultas()
    print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
    id_consulta = input(f"{Cores.BRIGHT_YELLOW}Digite o ID da consulta para remover: {Cores.RESET}")
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM consultas WHERE id=?', (id_consulta,))
    consulta = c.fetchone()
    
    if not consulta:
        print_erro("Consulta não encontrada!")
    else:
        confirmacao = input(f"{Cores.BRIGHT_RED}Tem certeza que deseja remover a consulta ID {consulta[0]}? (s/n): {Cores.RESET}").lower()
        if confirmacao == 's':
            c.execute('DELETE FROM consultas WHERE id=?', (id_consulta,))
            conn.commit()
            print_sucesso("Consulta removida com sucesso!")
        else:
            print_info("Operação cancelada.")
    
    conn.close()
    aguardar_enter()

def mostrar_creditos():
    """Exibe informações do autor"""
    print_titulo('Informações do Autor')
    print(f"{Cores.BRIGHT_CYAN}{'─'*60}{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}👨‍💻 Desenvolvedor:{Cores.RESET}")
    print(f"{Cores.BRIGHT_GREEN}   Willian de Aquino Faria Junior{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}🎓 RU:{Cores.RESET}")
    print(f"{Cores.BRIGHT_GREEN}   4364310{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}🏥 Sistema:{Cores.RESET}")
    print(f"{Cores.BRIGHT_GREEN}   SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde{Cores.RESET}")
    print(f"{Cores.BRIGHT_MAGENTA}{Cores.BOLD}📅 Versão:{Cores.RESET}")
    print(f"{Cores.BRIGHT_GREEN}   1.0 - Terminal Interface{Cores.RESET}")
    print(f"{Cores.BRIGHT_CYAN}{'─'*60}{Cores.RESET}")
    aguardar_enter()

def menu_principal():
    while True:
        print_titulo('SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde')
        print_menu_titulo("Menu Principal")
        
        print_opcao_menu("1", "Gerenciar Pacientes", Icones.USER)
        print_opcao_menu("2", "Gerenciar Profissionais", Icones.DOCTOR)
        print_opcao_menu("3", "Gerenciar Leitos", Icones.BED)
        print_opcao_menu("4", "Gerenciar Consultas", Icones.CALENDAR)
        print_opcao_menu("5", "Informações do Autor", "👨‍💻")
        print_opcao_menu("0", "Sair do Sistema")
        
        print(f"\n{Cores.BRIGHT_CYAN}{'─'*50}{Cores.RESET}")
        op = input(f"{Cores.BRIGHT_YELLOW}Escolha uma opção: {Cores.RESET}")
        
        if op == '1':
            menu_pacientes()
        elif op == '2':
            menu_profissionais()
        elif op == '3':
            menu_leitos()
        elif op == '4':
            menu_consultas()
        elif op == '5':
            mostrar_creditos()
        elif op == '0':
            print(f"\n{Cores.BRIGHT_CYAN}{Icones.HEART} Obrigado por usar o SGHSS! {Icones.HEART}{Cores.RESET}")
            print(f"{Cores.BRIGHT_GREEN}Desenvolvido por: Willian de Aquino Faria Junior - RU: 4364310{Cores.RESET}")
            animacao_carregamento("Encerrando sistema", 1)
            sys.exit()
        else:
            print_erro("Opção inválida!")
            aguardar_enter()

if __name__ == "__main__":
    try:
        criar_tabelas()
        print(f"{Cores.BRIGHT_CYAN}{Icones.HOSPITAL} Iniciando SGHSS - Sistema de Gestão Hospitalar {Icones.HOSPITAL}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}Desenvolvido por: Willian de Aquino Faria Junior - RU: 4364310{Cores.RESET}")
        animacao_carregamento("Inicializando sistema", 2)
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.BRIGHT_CYAN}{Icones.HEART} Sistema encerrado pelo usuário. Obrigado! {Icones.HEART}{Cores.RESET}")
        print(f"{Cores.BRIGHT_GREEN}Desenvolvido por: Willian de Aquino Faria Junior - RU: 4364310{Cores.RESET}")
    except Exception as e:
        print(f"\n{Cores.BRIGHT_RED}{Icones.ERROR} Erro inesperado: {e}{Cores.RESET}")
        input("Pressione Enter para sair...") 