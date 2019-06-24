def criar_tabela_resultados():
    return """CREATE TABLE IF NOT EXISTS resultados (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        latitude VARCHAR(20),
                                        longitude VARCHAR(20),
                                        rua VARCHAR(100),
                                        numero VARCHAR(15),
                                        bairro VARCHAR(50),
                                        cidade VARCHAR(50),
                                        cep VARCHAR(50),
                                        uf VARCHAR(10),
                                        pais VARCHAR(100)
                                    );"""


def insert_resultados(endereco: dict):
    return f"""INSERT INTO resultados
                    (latitude, longitude, rua, numero, bairro, cidade, cep, uf, pais)
                VALUES
                    ('{endereco["latitude"]}', '{endereco["longitude"]}', '{str(endereco["rua"]).replace("'", " ")}', 
                        '{endereco["numero"]}', '{str(endereco["bairro"]).replace("'", " ")}', '{str(endereco["cidade"]).replace("'", " ")}',
                        '{endereco["cep"]}', '{endereco["uf"]}', '{endereco["pais"]}');"""