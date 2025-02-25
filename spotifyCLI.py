import click

@click.command()
@click.argument("song")
def play(song):
    click.echo(f"playing {song}")

@click.command()
def pause():
    click.echo("paused")

@click.group()
def cli():
    pass

cli.add_command(play)
cli.add_command(pause)

if __name__ == "__main__":
    cli()
