import pathlib
import click
import os
from os import scandir
from datetime import datetime


def convert_date(timestamp: datetime) -> str:
    d: datetime = datetime.utcfromtimestamp(timestamp)
    formated_date: datetime = d.strftime('%d %b %Y')

    return formated_date


@click.command(name='list_files')
@click.pass_obj
def cli(obj: pathlib.Path) -> None:
    """ List all files from a directory"""
    # Verify if the directory exists
    dir_files = scandir(obj.dir)
    if os.path.isdir(obj.dir):
        for file in dir_files:
            # Verify if the file exist in the current directory
            if file.is_file():
                info = file.stat()
                click.secho(f'{file.name} \t\t'
                            f'Last Modified: {convert_date(info.st_mtime)} \t'
                            f'Size: {info.st_size} bytes', fg='bright_yellow')
