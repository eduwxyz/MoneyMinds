import json

import typer


class Moneyminds:
    def __init__(self, db_path: str):
        self.db_path = db_path
        
        
        
    def add_json(self, valor: float, descricao: str, categoria: str):
        
        with open(self.db_path, "w") as f:
            feeds = json.load(f)
            
            data = {"valor": valor, "descricao": descricao, "categoria": categoria}
            feeds.append(data)
            
            with open(self.db_path, "w") as f:
                json.dump(feeds, f, indent=4)
            
            
            
            
    def view_json(self, db_path: str):
        with open(db_path, "r") as f:
            data = json.load(f)
            
        typer.echo(f"Valor: {data['valor']}")
        typer.echo(f"Descrição: {data['descricao']}")
        typer.echo(f"Categoria: {data['categoria']}")