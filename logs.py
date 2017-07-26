#!/usr/bin/env python

import psycopg2


def connect(database_name="news"):
    """Connect to given PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={dbname}".format(dbname=database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception, error:
        print error


def execute_query(query):
    """Executes a query and return it's results"""
    db, cursor = connect()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def print_output(results, ext):
    """Writes results from execute_query in a file"""
    f = open("output.txt", "a")
    for line in results:
        f.write("{}     - {}{}\n".format(str(line[0]), str(line[1]), str(ext)))
    f.close()

# Most popular three articles of all time:
query_1 = (
    "select articles.title, count(*) as num_views from articles \
    inner join log on log.path = concat('/article/', articles.slug) \
    group by articles.title, log.path order by num_views desc limit 3"
)

# Most popular authors of all time
query_2 = (
    "select authors.name, count(*) as num_views from articles \
    inner join authors on authors.id= articles.author \
    inner join log on log.path = concat('/article/', articles.slug) \
    group by authors.name, log.path order by num_views desc limit 4"
)

# Days with more than 1% failed requests

query_3 = (
    "select to_char(a.date, 'Mon DD, YYYY'), \
    round(a.errors * 100.0 / b.requests, 2) \
       from (select time::date as date, count(*) as errors \
             from log \
             where status != '200 OK' \
             group by date) as a, \
            (select time::date as date, count(*) as requests \
             from log \
             group by date) as b \
       where a.date = b.date \
       and (a.errors * 100.0 / b.requests) >= 1;"
)

if __name__ == '__main__':
    # Problem 1
    f = open("output.txt", "w")
    f.write("What are the most popular three articles of all time?\n")
    f.close()

    results = execute_query(query_1)
    print_output(results, " views")

    # Problem 2
    f = open("output.txt", "a")
    f.write("\n\nWho are the most popular article authors of all time?\n")
    f.close()

    results = execute_query(query_2)
    print_output(results, " views")

    # Problem 3
    f = open("output.txt", "a")
    f.write("\n\nOn which days did more than 1% of requests lead to errors?\n")
    f.close()

    results = execute_query(query_3)
    print_output(results, "% errors")
