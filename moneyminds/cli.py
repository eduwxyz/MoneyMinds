import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from moneyminds.api import Moneyminds
from moneyminds import ERRORS, config, database

app = typer.Typer()


@app.command()
def init(db_path: str = typer.Option(default=str(database.DEFAULT_DB_FILE_PATH), prompt=True)):
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.echo(f"Creating config file failed with {ERRORS[app_init_error]}")
        raise typer.Abort()
    
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.echo(f"Creating database file failed with {ERRORS[db_init_error]}")
        raise typer.Abort()
    
    else:
        typer.echo(f"Config file created successfully {db_path}")


@app.command()
def add_to_json(valor: Annotated[float, typer.Option(prompt=True)], 
                categoria: Annotated[str, typer.Option(prompt=True)], 
                descricao: Annotated[str, typer.Option(prompt=True)], 
            
):
    
    #entrada: Annotated[bool, typer.Option(prompt=True)],
    
    # with open("moneymins.json", "w") as f:
    #     f.write(json.dumps({"valor": valor, "categoria": categoria, "descricao": descricao, "entrada": entrada}))
    
    carteira = Moneyminds("/home/eduarodomachado/.eduarodomachado_moneyminds.json")
    carteira.add_json(valor, descricao, categoria)
    carteira.view_json("/home/eduarodomachado/.eduarodomachado_moneyminds.json")
    

@app.command()
def view_data():
    with open("moneymins.json", "r") as f:
        data = json.load(f)
        
        
    
    Console().print("[bold magenta]Todos[/bold magenta]!", "💻")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Valor", style="dim", width=12)
    table.add_column("Categoria")
    table.add_column("Descrição")
    table.add_column("Entrada")
    
    table.add_row(str(data["valor"]), data["categoria"], data["descricao"], str(data["entrada"]))
    Console().print(table)



if __name__ == "__main__":
    app()