from pymongo import MongoClient

import csv
import json

csvfile = open('items.csv', 'r')
jsonfile = open('file.json', 'w')
client = MongoClient("mongodb://localhost")
db = client.teg

fieldnames = ('DRE', 'CD_ESC', 'TIPO_ESC', 'NOME_ESC', 'LAT_ESC', 'LON_ESC',

              'CD_TURM', 'DESC_TURMA',
              'DESC_TURNO', 'MODALIDADE',
              'CD_SERIE', 'DESC_SERIE',
              'CD_ALUNO', 'IDADE_ALUNO',
              'DEFIC',
              'DESC_DEFIC',
              'CADEIRANTE', 'ALUNO_TEG',
              'DESC_MOTIVO_INCLUSAO', 'LAT_ALUN', 'LON_ALUN',
              'DATABAS'
              )
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    coord = [int(row['LAT_ESC']), int(row['LON_ESC'])]
    
    school = {
        'CD_ESC' : row['CD_ESC'],
        'TIPO_ESC': row['TIPO_ESC'],
        'NOME_ESC': row['NOME_ESC'],
        'PLACE': {
            'type': "Point",
            'coordinates': coord
        }
    }
    
    db.schools.update({'CD_ESC': school.get('CD_ESC')}, school, True)

    
    student = {
        'CD_TURM': row['CD_TURM'],
        'DESC_TURMA': row['DESC_TURMA'],
        'DESC_TURNO': row['DESC_TURNO'],
        'MODALIDADE': row['MODALIDADE'],
        'CD_SERIE': row['CD_SERIE'],
        'DESC_SERIE': row['DESC_SERIE'],
        'CD_ALUNO': row['CD_ALUNO'],
        'IDADE_ALUNO': row['IDADE_ALUNO'],
        'DEFIC': row['DEFIC'],
        'DESC_DEFIC': row['DESC_DEFIC'],
        'CADEIRANTE': row['CADEIRANTE'],
        'ALUNO_TEG': row['ALUNO_TEG'],
        'DESC_MOTIVO_INCLUSAO': row['DESC_MOTIVO_INCLUSAO'],
        'PLACE': {
            'type': "Point",
            'coordinates': [ int(row['LAT_ALUN']), int(row['LON_ALUN'])]
        },
        'DATABAS': row['DATABAS']
    }

    
    db.students.update({'CD_ALUNO': student.get('CD_ALUNO')}, student, True)

print('schools', (db.schools.count()))
print('students', (db.schools.count()))
    