import click
from pathlib import Path
from datetime import datetime
import time
import sqlite3
import os


@click.command()
@click.argument("path")
@click.version_option("0.0.10", prog_name="hello")
def hello(path):
    '''
        This command prints the message "Hello World"
    '''
    click.echo("Hello World")
    target_dir = Path(path)
    
    for entry in target_dir.iterdir():
        click.echo(entry)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', default="", help='Name of Database')
@click.argument('name')
def initdb(name):
    click.echo('initialized the database')
    
    try:
        if os.path.isfile(name + '.db'):
            click.echo('Database exists')
            return False
        if not os.path.isfile(name + '.db'):
            click.echo('Database doesnt exist')
            click.echo('Creating Database')
            con = sqlite3.connect('todo.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE todo(title, description, category)')
            con.commit()
            click.echo("Database Created")
    except Exception as e:
        raise e

@cli.command()
def dropdb():
    click.echo('dropped database')
    with click.progressbar([1,2,3,4,5]) as bar:
        for x in bar:
            print(f'sleep({x})')
            time.sleep(1)

@cli.command()
@click.option('--timenow', default='text', help='Give time now')
@click.argument('timenow')
def timenow(timenow):
    click.echo(f'{datetime.now()}')
    click.echo(f'Time now is : {timenow}')

if __name__ == '__main__':
    cli()
