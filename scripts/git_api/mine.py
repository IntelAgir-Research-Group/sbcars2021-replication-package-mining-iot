import json
import sqlite3

#Abrindo arquivo json e carregando com load na variável dados -> dados.
with open('/home/michel/eclipse-workspace/mining/git_rest_api/internet_of_things/description/internet_of_things-1.json',encoding='utf-8') as json_file:
    dados = json.load(json_file)

#print(dados)

#Fazendo conexão com o banco de dados, mine_iot2021:
conn = sqlite3.connect('/home/michel/eclipse-workspace/mining/git_rest_api/mine_iot2021.db')
cursor = conn.cursor()

#Gerando a tabela commits:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS commits(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_github integer(240),
        username varchar(240),
        url varchar(240),
        creation varchar(240),
        description varchar(240),
        contributors varchar(240),
        language varchar(240),
        stars varchar(240),
        last_update datetime,
        commits varchar(240),
        issues varchar(240),
        wiki boolean,
        watchers integer,
        open_issues integer,
        score float
        );
    ''')

#Inserindo dados do json no Banco de Dados mine_iot2021 sqlite3:
for item in dados["items"]:

    cursor.execute("""
            INSERT INTO commits(id_github,username,url,creation,
                description,contributors,language,stars,
                last_update,commits,issues,wiki,watchers,open_issues,score)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,(item["id"],item["full_name"],item["html_url"],item["created_at"],
                         item["description"],item["collaborators_url"],item["language"],
                         item["stargazers_url"],item["updated_at"],item["commits_url"],item["issues_url"],
                         item["has_wiki"],item["watchers"],item["open_issues"],item["score"])
                )
    conn.commit()
#print('Dados inseridos com sucesso.')
conn.close()
