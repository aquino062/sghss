#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para adicionar dados de exemplo no banco de dados SGHSS

"""

import sqlite3
import sys
from datetime import datetime

DB_NAME = 'sghss_terminal.db'

def conectar():
    """Conecta ao banco de dados"""
    try:
        return sqlite3.connect(DB_NAME)
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def adicionar_pacientes():
    """Adiciona pacientes de exemplo"""
    conn = conectar()
    if not conn:
        return False
    
    try:
        c = conn.cursor()
        
        # Dados dos pacientes
        pacientes = [
            ('Ana Silva Santos', '11111111111', '1990-01-15', '11999990001', 'ana.silva@email.com'),
            ('Bruno Souza Costa', '22222222222', '1985-05-12', '11999990002', 'bruno.souza@email.com'),
            ('Carla Dias Oliveira', '33333333333', '1978-09-23', '11999990003', 'carla.dias@email.com'),
            ('Diego Lima Pereira', '44444444444', '2000-03-15', '11999990004', 'diego.lima@email.com'),
            ('Elisa Ramos Ferreira', '55555555555', '1995-07-30', '11999990005', 'elisa.ramos@email.com'),
            ('Fernando Alves Silva', '66666666666', '1982-11-08', '11999990006', 'fernando.alves@email.com'),
            ('Gabriela Costa Lima', '77777777777', '1992-04-20', '11999990007', 'gabriela.costa@email.com'),
            ('Henrique Santos Dias', '88888888888', '1988-12-03', '11999990008', 'henrique.santos@email.com')
        ]
        
        c.executemany('''
            INSERT OR IGNORE INTO pacientes (nome, cpf, data_nascimento, telefone, email) 
            VALUES (?, ?, ?, ?, ?)
        ''', pacientes)
        
        conn.commit()
        print(f"✅ {len(pacientes)} pacientes adicionados com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao adicionar pacientes: {e}")
        return False
    finally:
        conn.close()

def adicionar_profissionais():
    """Adiciona profissionais de exemplo"""
    conn = conectar()
    if not conn:
        return False
    
    try:
        c = conn.cursor()
        
        # Dados dos profissionais
        profissionais = [
            ('Dr. Carlos Mendes Silva', 'Médico', 'CRM12345', 'Cardiologia'),
            ('Dra. Fernanda Costa Lima', 'Médica', 'CRM12346', 'Pediatria'),
            ('Dr. Roberto Santos Oliveira', 'Médico', 'CRM12347', 'Ortopedia'),
            ('Enf. Maria Oliveira Silva', 'Enfermeira', 'COREN12345', 'UTI'),
            ('Enf. João Pereira Costa', 'Enfermeiro', 'COREN12346', 'Emergência'),
            ('Dra. Juliana Alves Dias', 'Médica', 'CRM12348', 'Ginecologia'),
            ('Dr. Pedro Lima Ferreira', 'Médico', 'CRM12349', 'Neurologia'),
            ('Enf. Ana Paula Santos', 'Enfermeira', 'COREN12347', 'Centro Cirúrgico')
        ]
        
        c.executemany('''
            INSERT OR IGNORE INTO profissionais (nome, cargo, registro, especialidade) 
            VALUES (?, ?, ?, ?)
        ''', profissionais)
        
        conn.commit()
        print(f"✅ {len(profissionais)} profissionais adicionados com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao adicionar profissionais: {e}")
        return False
    finally:
        conn.close()

def adicionar_leitos():
    """Adiciona leitos de exemplo"""
    conn = conectar()
    if not conn:
        return False
    
    try:
        c = conn.cursor()
        
        # Dados dos leitos
        leitos = [
            ('101', 'Enfermaria', 'Disponível'),
            ('102', 'Enfermaria', 'Disponível'),
            ('103', 'Enfermaria', 'Ocupado'),
            ('201', 'UTI', 'Disponível'),
            ('202', 'UTI', 'Ocupado'),
            ('203', 'UTI', 'Disponível'),
            ('301', 'Isolamento', 'Disponível'),
            ('302', 'Isolamento', 'Disponível'),
            ('401', 'Centro Cirúrgico', 'Disponível'),
            ('501', 'Emergência', 'Ocupado')
        ]
        
        c.executemany('''
            INSERT OR IGNORE INTO leitos (numero, tipo, status) 
            VALUES (?, ?, ?)
        ''', leitos)
        
        conn.commit()
        print(f"✅ {len(leitos)} leitos adicionados com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao adicionar leitos: {e}")
        return False
    finally:
        conn.close()

def adicionar_consultas():
    """Adiciona consultas de exemplo"""
    conn = conectar()
    if not conn:
        return False
    
    try:
        c = conn.cursor()
        
        # Primeiro, vamos pegar alguns IDs de pacientes e profissionais
        c.execute('SELECT id FROM pacientes LIMIT 5')
        pacientes_ids = [row[0] for row in c.fetchall()]
        
        c.execute('SELECT id FROM profissionais WHERE cargo LIKE "%Médic%" LIMIT 5')
        profissionais_ids = [row[0] for row in c.fetchall()]
        
        if not pacientes_ids or not profissionais_ids:
            print("❌ É necessário ter pacientes e profissionais cadastrados primeiro!")
            return False
        
        # Dados das consultas
        consultas = [
            (pacientes_ids[0], profissionais_ids[0], '2024-01-15 09:00:00', 'Consulta de rotina - Cardiologia'),
            (pacientes_ids[1], profissionais_ids[1], '2024-01-15 10:30:00', 'Consulta pediátrica'),
            (pacientes_ids[2], profissionais_ids[2], '2024-01-15 14:00:00', 'Avaliação ortopédica'),
            (pacientes_ids[3], profissionais_ids[0], '2024-01-16 08:00:00', 'Retorno cardiologia'),
            (pacientes_ids[4], profissionais_ids[1], '2024-01-16 11:00:00', 'Consulta pediátrica'),
            (pacientes_ids[0], profissionais_ids[2], '2024-01-17 15:30:00', 'Avaliação ortopédica'),
            (pacientes_ids[1], profissionais_ids[0], '2024-01-18 09:00:00', 'Consulta cardiologia'),
            (pacientes_ids[2], profissionais_ids[1], '2024-01-18 13:00:00', 'Retorno pediatria')
        ]
        
        c.executemany('''
            INSERT OR IGNORE INTO consultas (paciente_id, profissional_id, data_hora, motivo) 
            VALUES (?, ?, ?, ?)
        ''', consultas)
        
        conn.commit()
        print(f"✅ {len(consultas)} consultas adicionadas com sucesso!")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao adicionar consultas: {e}")
        return False
    finally:
        conn.close()

def mostrar_estatisticas():
    """Mostra estatísticas do banco de dados"""
    conn = conectar()
    if not conn:
        return
    
    try:
        c = conn.cursor()
        
        print("\n" + "="*50)
        print("📊 ESTATÍSTICAS DO BANCO DE DADOS")
        print("="*50)
        
        # Contar registros em cada tabela
        tabelas = ['pacientes', 'profissionais', 'leitos', 'consultas']
        for tabela in tabelas:
            c.execute(f'SELECT COUNT(*) FROM {tabela}')
            count = c.fetchone()[0]
            print(f"📋 {tabela.capitalize()}: {count} registros")
        
        print("="*50)
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao mostrar estatísticas: {e}")
    finally:
        conn.close()

def main():
    """Função principal"""
    print("🏥 SGHSS - Adicionando Dados de Exemplo")
    print("="*50)
    
    # Adicionar dados em ordem (primeiro as tabelas independentes)
    sucessos = 0
    
    print("\n1️⃣ Adicionando pacientes...")
    if adicionar_pacientes():
        sucessos += 1
    
    print("\n2️⃣ Adicionando profissionais...")
    if adicionar_profissionais():
        sucessos += 1
    
    print("\n3️⃣ Adicionando leitos...")
    if adicionar_leitos():
        sucessos += 1
    
    print("\n4️⃣ Adicionando consultas...")
    if adicionar_consultas():
        sucessos += 1
    
    # Mostrar estatísticas finais
    mostrar_estatisticas()
    
    print(f"\n🎉 Processo concluído! {sucessos}/4 operações realizadas com sucesso.")
    print("\n💡 Dica: Execute o arquivo 'sghss_terminal.py' para acessar o sistema!")

if __name__ == "__main__":
    main() 