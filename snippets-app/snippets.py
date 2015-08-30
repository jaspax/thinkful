import sys
import logging
import argparse
import psycopg2

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def getDb():
    """Get a connection to the snippets db"""
    return psycopg2.connect("dbname='snippets'")

def putSnippet(name, snippet):
    """Store a snippet with an associated name"""
    conn = getDb()
    cursor = conn.cursor()
    sql = "insert into snippets values(%s, %s)"
    logging.debug("executing sql: {}".format(sql))
    cursor.execute(sql, (name, snippet))
    conn.commit()
    logging.debug("successfully stored snippet")

def getSnippet(name):
    """Get a snippet with a given name"""
    conn = getDb()
    cursor = conn.cursor()
    sql = "select message from snippets where name = %s"
    logging.debug("executing sql: {}".format(sql))
    cursor.execute(sql, (name,))
    row = cursor.fetchone()
    if (not row):
        print "No snippet matching '{}' found".format(name)
    else:
        print row[0]

def listSnippets(pattern=''):
    """list snippets optionally matching a pattern"""
    conn = getDb()
    cursor = conn.cursor()
    if (pattern):
        sql = "select name from snippets where name ilike %s"
    else:
        sql = "select name from snippets"

    logging.debug("executing sql: {}".format(sql))
    cursor.execute(sql, (pattern,))
    for row in cursor:
        print row[0]
    return row[0]

def commandNotFound():
    """runs when a command isn't found"""
    print "Doesn't exist, yo"

def buildParser():
    parser = argparse.ArgumentParser(description="Store and retrieve chunks of texty text")
    subparsers = parser.add_subparsers(dest="command", help="Commands implemented by this program")

    put_cmd = subparsers.add_parser("put", help="store a snippet")
    put_cmd.add_argument("name", help="name of the snippet to store")
    put_cmd.add_argument("snippet", help="the content of the snippet to store")

    get_cmd = subparsers.add_parser("get", help="get a snippet by name")
    get_cmd.add_argument("name", help="name of the snippet to retrieve")

    list_cmd = subparsers.add_parser("list", help="get the snippets whose names match a pattern")
    #list_cmd.add_argument("list", help="the pattern to match. may be omitted to return all snippets", default='')

    return parser

def main():
    logging.info("constructing parser")
    parser = buildParser()
    args = vars(parser.parse_args(sys.argv[1:]))

    # Let's be fancy, mmkay?
    {
        "put": putSnippet,
        "get": getSnippet,
        "list": listSnippets,
    }.get(args.pop("command"))(**args)


if __name__ == "__main__":
    main()
