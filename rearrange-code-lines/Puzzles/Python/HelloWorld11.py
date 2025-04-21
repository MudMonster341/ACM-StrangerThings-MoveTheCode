import click

@click.command()
@click.option("--count", default=1, help="Number of greetings")
def hello(count):
    for _ in range(count):
        click.echo("Hello!")

if __name__ == "__main__":
    hello()
