import click
import pathlib
import os
from os import scandir

from click.types import DateTime

def convert_date(timestamp) -> str:
    d = DateTime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    
    return formated_date


@click.command(name='list_files')
@click.pass_obj
def cli(obj):
    """ List all files from a directory"""
    # Verify if the directory exists
    dir_files = scandir(obj.dir)
    if os.path.isdir(obj.dir):
        for file in dir_files:
            # Verify if the file exist in the current directory
            if file.is_file():
                info = file.stat()
                click.secho(f'{file.name} \t\t Last Modified: {convert_date(info.st_mtime)} \t Size: {info.st_size} bytes', fg='bright_yellow')