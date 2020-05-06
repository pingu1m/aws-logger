from clog.commands.config import get_parser as config
from clog.commands.get import get_parser as get
from clog.commands.put import get_parser as put
from clog.commands.rm import get_parser as rm

def hello():
    print("hello from new cli app")

def get_parsers():
    return [config(), get(), put(), rm()]
