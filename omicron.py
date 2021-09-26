import click
import os.path
import shutil
from pathlib import Path

def verify_dir(directory):
    if  os.path.isdir(directory):
        return True
    else:
        return False

def fileAtLocation(filename, path):
    if os.path.exists(path + "/" + filename):
        return True

# Verifica se o nome do arquivo realmente é um arquivo existe
def verify_file(filename) -> bool:
    if os.path.isfile(filename):
        return True
    else:
        return False

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
@click.option('-fl', '--filename', type=str, required=True )
@click.option('-fr', '--fromn', type=str, required=True)
@click.option('-t', '--to', type=str, required=True )
def move_file(filename, fromn , to):
    """Move a file from a  directory to another"""
    if(verify_file(filename) and verify_dir(fromn) and verify_dir(to)):
        shutil.move(filename, to)
        click.secho(f'{filename} moved to {to}', fg='green')



@click.command(name='delete')
@click.option('-f', '--filename', type=str, required=True)
@click.option('-d', '--directory', type=str, required=True)
def delete_file(filename, directory):
    """Delete a file from a directory"""
    # if the file is in the current directory, delete it
    if fileAtLocation(filename, directory):
        os.remove(directory + "/" + filename)
        click.secho(f'{filename} deleted', fg='green')



@click.command(name='listFiles')
@click.option('-d', '--directory', type=str, required=True)
def listFiles(directory):
    """ List all files from a directory"""
    # Verify if the directory exists
    if verify_dir(directory):
        for file in os.listdir(directory):
            # Verify if the file exist in the current directory
            if fileAtLocation(file, directory):
                click.secho(f'{file}', fg='yellow')


@click.command(name='organize')
@click.option('-d', '--directory', type=str, required=True)
def organize(directory): 
    """ Organize all files from a directory """
    if verify_dir(directory):
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



options.add_command(listFiles)
options.add_command(organize)
options.add_command(move_file)
options.add_command(delete_file)
omicron.add_command(options)


if __name__ == '__main__':
    omicron()