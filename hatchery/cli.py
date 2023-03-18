from loguru import logger
import click
from flask.cli import FlaskGroup, get_version as get_flask_version
from flask.cli import pass_script_info
from . import __version__
from .server.app import create_app


def get_version(ctx, param, value):
    click.echo(
        f"Hatchery Visualization {__version__}",
        color=ctx.color,
    )
    get_flask_version(ctx, param, value)


@click.group(cls=FlaskGroup, add_version_option=False, create_app=create_app)
@click.option('--version', help="Show the flask version",
              expose_value=False,
              callback=get_version,
              is_flag=True,
              is_eager=True,)
@pass_script_info
def cli(info, **kwargs):
    """
       Management script for Color Report application.
    """
    logger.info('Starting cli')
