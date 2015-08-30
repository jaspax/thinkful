import logging
import argparse

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def putSnippet(name, snippet):
    """Store a snippet with an associated name"""
    logging.error("{0} notimpl", putSnippet.__name__)

def getSnippet(name, snippet):
    """Get a snippet with a given name"""
    logging.error("{0} notimpl"), getSnippet.__name__)

def listSnippets(pattern):
    """list snippets optionally matching a pattern"""
    logging.error("{0} notimpl"), listSnippets.__name__)

def buildParser():
    parser = argparse.ArgumentParser(description="Store and retrieve chunks of texty text")
    subparsers = parse.add_subparsers(dest="command", help="Commands implemented by this program")

    put_cmd = subparsers.add_parser("put", help="store a snippet")
    put_cmd.add_argument("name", help="name of the snippet to store")
    put_cmd.add_argument("snippet", help="the content of the snippet to store")

    get_cmd = subparsers.add_parser("cmd", help="get a snippet by name")
    get_cmd.add_argument("name", help="name of the snippet to retrieve")

def main():
    logging.info("constructing parser")
    parser = buildParser()
    args = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()
