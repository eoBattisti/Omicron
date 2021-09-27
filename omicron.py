from os import scandir
import os
import pathlib
import click
import os.path
import shutil
import zipfile

from datetime import datetime
from pathlib import Path


def fileAtLocation(filename, path):
    if os.path.exists(path + "/" + filename):
        return True
    else:
        click.secho(f'{filename} is not in {path}, please enter a valid filename', fg='bright_red')
# Verifica se o nome do arquivo realmente é um arquivo existe

def isImage(file) -> bool:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".svg") or file.endswith(".jpeg") or file.endswith(".gif")  or file.endswith(".ico"): 
        return True 
    else:
        return False
            
def isPDF(file) -> bool:
    return True if file.endswith(".pdf") else False

def isSheet(file) ->  bool:
    return True if file.endswith(".csv") or file.endswith(".xls") or file.endswith(".xlsx") else False

def isDocOrDocx(file) -> bool:
    return True if file.endswith(".doc") or file.endswith(".docx") else False

def isPptOrPptx(file) -> bool:
    return True if file.endswith(".ppt") or file.endswith(".pptx") else False

def isZipOrRar(file) -> bool:
    return True if file.endswith(".zip") or file.endswith(".rar") else False


def convertDate(timestamp) -> str:
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    
    return formated_date




@click.group()
def omicron():
    '''
    Here are the commands to manage the CLI
    '''
    
@click.group(name='options')
def options():
    '''
    Group the commands to do something with files
    '''
    pass


# Move a file to a directory
@click.command(name='move')
@click.argument('filename', type=str, nargs=1, required=True)
@click.argument('dict_too', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True )
def move_file(filename, dict_from , dict_too):
    """Move a file from a  directory to another"""
    if os.path.isfile(filename):
        shutil.move(filename,dict_too)
        click.secho(f'{filename} moved to {dict_too}', fg='green')



@click.command(name='delete')
@click.argument('directory', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True)
@click.option('--all/--one', default=False, help="Delete one file or all file's directory")
def delete_file(directory, all):
    """Delete a file from a directory"""
    # Delete all files from a directory
    if all:
        if click.confirm(click.style(f'This option wil delete all files from {directory}?', fg='bright_cyan'), abort=True):
            for files in os.listdir(directory):
                os.remove(directory + "/" + files)
                click.secho(f'{files}: successfully deleted', fg='green')
    else:
        
        filename = click.prompt(click.style("What file you want to remove", fg='bright_cyan'), type=str)
        # if the file is in the current directory, delete it
        if fileAtLocation(filename, directory):
            os.remove(directory + "/" + filename)
            click.secho(f'{filename} deleted', fg='green')


@click.command(name='listFiles')
@click.argument('directory', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True)
def listFiles(directory):
    """ List all files from a directory"""
    # Verify if the directory exists
    dir_files = scandir(directory)
    if os.path.isdir(directory):
        for file in dir_files:
            # Verify if the file exist in the current directory
            if file.is_file():
                info = file.stat()
                click.secho(f'{file.name} \t\t Last Modified: {convertDate(info.st_mtime)} \t Size: {info.st_size} bytes', fg='bright_yellow')


@click.command(name='organize')
@click.argument('directory', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True)
def organize(directory): 
    """ Organize all files from a directory """
    for file in os.listdir(directory):
        if fileAtLocation(file, directory):
            # Identify if the file is an Image .jpg .png .jpeg .svg .gif or .ico
            if isImage(file):
                path = Path(directory + "/" + "Images/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if the file is an PDF .pdf
            if isPDF(file):
                path = Path(directory + "/" + "PDFs/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is an Sheet .xls, .xlsx or .csv 
            if isSheet(file):
                path = Path(directory + "/" + "Sheets/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .doc or .docx
            if isDocOrDocx(file):
                path = Path(directory + "/" + "Docs/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .ppt or .pptx
            if isPptOrPptx(file):
                path = Path(directory + "/" + "Slides/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .zip or .rar
            if isZipOrRar(file):
                path = Path(directory + "/" + "Zips/")
                file = directory + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

@click.command()
@click.argument('filename', nargs=1, required=True)
@click.argument('directory', type=click.Path(exists=True, allow_dash=True, path_type=pathlib.Path), required=True)
def extract(filename, directory):
    """Extract a .zip or .rar files in a directory """
    if os.path.isfile(filename):
        filename = zipfile.ZipFile(filename, 'r')
        filename.extractall(path=directory)
        click.secho(f'File successfully extracted', fg='bright_green')



options.add_command(listFiles)
options.add_command(organize)
options.add_command(move_file)
options.add_command(delete_file)
options.add_command(extract)
omicron.add_command(options)


if __name__ == '__main__':
    omicron()