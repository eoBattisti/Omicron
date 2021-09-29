import click
import os

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class Omicron(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']
            

class Directory(object):
    def __init__(self, dir=None):
        self.dir = os.path.abspath(dir or '.') 


@click.group(cls=Omicron, help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.' )
@click.pass_context
@click.option('-d', '--dir', help='This will be the main directory that u will be able to delete, extract, list, move, or organize')
def cli(ctx, dir):
    ctx.obj = Directory(dir)




if __name__ == '__main__':
    cli()