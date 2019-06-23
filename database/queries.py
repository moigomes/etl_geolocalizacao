def criar_tabela_resultados():
    return """CREATE TABLE IF NOT EXISTS resultados (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        latitude text,
                                        longitude text,
                                        rua text,
                                        numero text,
                                        bairro text,
                                        cidade text,
                                        cep text,
                                        uf text,
                                        pais text
                                    );"""


def insert_resultados(endereco: dict):
    return f"""INSERT INTO resultados
                    (latitude, longitude, rua, numero, bairro, cidade, cep, uf, pais)
                VALUES
                    ('{endereco["latitude"]}', '{endereco["longitude"]}', '{endereco["rua"]}', 
                        '{endereco["numero"]}', '{str(endereco["bairro"]).replace("'", " ")}', '{endereco["cidade"]}',
                        '{endereco["cep"]}', '{endereco["uf"]}', '{endereco["pais"]}');"""