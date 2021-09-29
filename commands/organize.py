import click
import pathlib
import os
import shutil

import os.path


def file_at_location(filename, path):
    if os.path.exists(path + "/" + filename):
        return True
    else:
        click.secho(f'{filename} is not in {path}, please enter a valid filename', fg='bright_red')

def is_image(file) -> bool:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".svg") or file.endswith(".jpeg") or file.endswith(".gif")  or file.endswith(".ico"): 
        return True 
    else:
        return False
            
def is_pdf(file) -> bool:
    return True if file.endswith(".pdf") else False

def is_sheet(file) ->  bool:
    return True if file.endswith(".csv") or file.endswith(".xls") or file.endswith(".xlsx") else False

def is_doc_or_docx(file) -> bool:
    return True if file.endswith(".doc") or file.endswith(".docx") else False

def is_ppt_or_pptx(file) -> bool:
    return True if file.endswith(".ppt") or file.endswith(".pptx") else False

def is_zip_or_rar(file) -> bool:
    return True if file.endswith(".zip") or file.endswith(".rar") else False

@click.command(name='organize')
@click.pass_obj
def cli(obj): 
    """ Organize all files from a directory """
    for file in os.listdir(obj.dir):
        if file_at_location(file, obj.dir):
            # Identify if the file is an Image .jpg .png .jpeg .svg .gif or .ico
            if is_image(file):
                path = pathlib.Path(obj.dir + "/" + "Images/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if the file is an PDF .pdf
            if is_pdf(file):
                path = pathlib.Path(obj.dir + "/" + "PDFs/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is an Sheet .xls, .xlsx or .csv 
            if is_sheet(file):
                path = pathlib.Path(obj.dir + "/" + "Sheets/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .doc or .docx
            if is_doc_or_docx(file):
                path = pathlib.Path(obj.dir + "/" + "Docs/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .ppt or .pptx
            if is_ppt_or_pptx(file):
                path = pathlib.Path(obj.dir + "/" + "Slides/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)

            # Identify if a file is .zip or .rar
            if is_zip_or_rar(file):
                path = pathlib.Path(obj.dir + "/" + "Zips/")
                file = obj.dir + "/" + file
                path.mkdir(exist_ok=True)
                shutil.move(file, path)