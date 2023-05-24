from neo4j import GraphDatabase

# Função para criar os nós e conexões
def criar_nos_e_conexoes():
    # Conectando ao banco de dados do Neo4j
    driver = GraphDatabase.driver("neo4j://localhost:7474", auth=("neo4j", "bdag2018"))

    # Abrindo uma sessão no banco de dados
    with driver.session() as session:
        # Criando os nós
        session.run("CREATE (t:Nodo {nome: 'Tupã'})")
        session.run("CREATE (i:Nodo {nome: 'Iacri'})")
        session.run("CREATE (b:Nodo {nome: 'Bastos'})")
        session.run("CREATE (r:Nodo {nome: 'Rancharia'})")
        session.run("CREATE (m:Nodo {nome: 'Martinópolis'})")
        session.run("CREATE (p1:Nodo {nome: 'Presidente Prudente'})")
        session.run("CREATE (p2:Nodo {nome: 'Presidente Bernardes'})")
        session.run("CREATE (s:Nodo {nome: 'Santo Anastácio'})")

        # Criando as conexões entre os nós
        session.run("MATCH (t:Nodo {nome: 'Tupã'}), (i:Nodo {nome: 'Iacri'}) CREATE (t)-[:CONEXAO]->(i)")
        session.run("MATCH (i:Nodo {nome: 'Iacri'}), (b:Nodo {nome: 'Bastos'}) CREATE (i)-[:CONEXAO]->(b)")
        session.run("MATCH (b:Nodo {nome: 'Bastos'}), (r:Nodo {nome: 'Rancharia'}) CREATE (b)-[:CONEXAO]->(r)")
        session.run("MATCH (r:Nodo {nome: 'Rancharia'}), (m:Nodo {nome: 'Martinópolis'}) CREATE (r)-[:CONEXAO]->(m)")
        session.run("MATCH (m:Nodo {nome: 'Martinópolis'}), (p1:Nodo {nome: 'Presidente Prudente'}) CREATE (m)-[:CONEXAO]->(p1)")
        session.run("MATCH (p1:Nodo {nome: 'Presidente Prudente'}), (p2:Nodo {nome: 'Presidente Bernardes'}) CREATE (p1)-[:CONEXAO]->(p2)")
        session.run("MATCH (p2:Nodo {nome: 'Presidente Bernardes'}), (s:Nodo {nome: 'Santo Anastácio'}) CREATE (p2)-[:CONEXAO]->(s)")

    # Fechando a conexão com o banco de dados
    driver.close()

# Chamando a função para criar os nós e conexões
criar_nos_e_conexoes()