
from flask import Blueprint

from .ext import InvenioJSONSchemasState

def create_blueprint(state: InvenioJSONSchemasState) -> Blueprint: ...
