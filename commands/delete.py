import click
import os
import pathlib

def file_at_location(filename: str, path: pathlib.Path) -> bool:
    if os.path.exists(path + "/" + filename):
        return True
    else:
        click.secho(f'{filename} is not in {path}, please enter a'
                    'valid filename', fg='bright_red')
        return False


@click.command(name='delete')
@click.option('--all/--one', default=False,
              help="Delete one file or all file's directory")
@click.pass_obj
def cli(obj: pathlib.Path, all: bool) -> None:
    """Delete a file from a directory"""

    if all:
        if click.confirm(click.style(f'This option wil delete all'
                                     f'files from {obj.dir}?',
                                     fg='bright_cyan'), abort=True):
            for files in os.listdir(obj.dir):
                os.remove(obj.dir + "/" + files)
                click.secho(f'{files}: successfully deleted', fg='bright_green')
    else:
        filename: str = click.prompt(click.style("What file you want to remove",
                                            fg='bright_cyan'), type=str)
        # if the file is in the current directory, delete it
        if file_at_location(filename, obj.dir):
            os.remove(obj.dir + "/" + filename)
            click.secho(f'{filename} deleted', fg='bright_green')
