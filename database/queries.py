def create_table_results():
    return """CREATE TABLE IF NOT EXISTS results (
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


def insert_results(adress):
    return f"""INSERT INTO results
                    (latitude, longitude, rua, numero, bairro, cidade, cep, uf, pais)
                VALUES
                    ('{adress["latitude"]}', '{adress["longitude"]}', '{adress["rua"]}', 
                        '{adress["numero"]}', '{str(adress["bairro"]).replace("'", " ")}', '{adress["cidade"]}',
                        '{adress["cep"]}', '{adress["uf"]}', '{adress["pais"]}');"""