import click

@click.group()
def cli():
    """This is a simple Click-based CLI tool."""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Greet a person by name."""
    click.echo(f"Hello, {name}!")

@cli.command()
def version():
    """Display the version of the CLI tool."""
    click.echo("MyCLI version 1.0")

if __name__ == '__main__':
    cli()
