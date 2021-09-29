import click
import os
import zipfile


@click.command()
@click.option('-f', '--filename', required=True, help="The filename that will be extracted")
@click.pass_obj
def cli(obj, filename):
    """Extract a .zip or .rar files in a directory """
    if os.path.isfile(filename):
        filename = zipfile.ZipFile(filename, 'r')
        filename.extractall(path=obj.dir)
        click.secho(f'File successfully extracted', fg='bright_green')