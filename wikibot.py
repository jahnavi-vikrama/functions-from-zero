from myLibrary.bot import scrape
import click


@click.command()
@click.option("--name", help="Web page we want to scrape")
@click.option("--length", help="Number of Sentences we want to scrape")
def cli(name, length):
    result = scrape(name,length)
    click.echo(click.style(f"{result}:", fg="blue"))


if __name__ == "__main__":
    cli()

