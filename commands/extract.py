import pathlib
import click
import os
import zipfile


@click.command()
@click.option('-f', '--filename', required=True,
              help="The filename that will be extracted")
@click.pass_obj
def cli(obj: pathlib.Path, filename: str) -> None:
    """Extract a .zip or .rar files in a directory """
    src = obj.dir + "/" + filename 
    if os.path.isfile(src):
        filename = zipfile.ZipFile(src, 'r')
        filename.extractall(path=obj.dir)
        click.secho("File successfully extracted", fg='bright_green')
