import click
import pathlib
import os
import shutil


@click.command(name='move')
@click.option('-f', '--filename', type=str, nargs=1, required=True, help="Filename that will be moved")
@click.option('-dst', '--destiny', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True, help="Directory where that the file will be moved" )
@click.pass_obj
def cli(obj, filename, destiny):
    """Move a file from a  directory to another"""
    # if the obj.dir instantiated is a valid dir and the filename is a valid file in the same
    # directory, move the file to the destiny
    if os.path.isdir(obj.dir):
        src = obj.dir + "/" + filename 
        if os.path.isfile(src):
            shutil.move(src, destiny)
            click.secho(f'{filename} moved to {destiny}', fg='green')
        else:
            click.secho("isnt a file")
    else:
        click.secho(f'error ocurred')