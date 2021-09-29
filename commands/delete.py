import click
import os


def file_at_location(filename, path):
    if os.path.exists(path + "/" + filename):
        return True
    else:
        click.secho(f'{filename} is not in {path}, please enter a valid filename', fg='bright_red')

@click.command(name='delete')
@click.option('--all/--one', default=False, help="Delete one file or all file's directory")
@click.pass_obj
def cli(obj, all):
    """Delete a file from a directory"""
    # Delete all files from a directory
    if all:
        if click.confirm(click.style(f'This option wil delete all files from {obj.dir}?', fg='bright_cyan'), abort=True):
            for files in os.listdir(obj.dir):
                os.remove(obj.dir + "/" + files)
                click.secho(f'{files}: successfully deleted', fg='green')
    else:
        
        filename = click.prompt(click.style("What file you want to remove", fg='bright_cyan'), type=str)
        # if the file is in the current directory, delete it
        if file_at_location(filename, obj.dir):
            os.remove(obj.dir + "/" + filename)
            click.secho(f'{filename} deleted', fg='green')