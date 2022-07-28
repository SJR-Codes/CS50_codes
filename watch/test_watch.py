"""
* CS50P Problem Set 7
* Test Watch on YouTube
* by Samu Reinikainen 28.07.2022
"""

from watch import parse

def test_valid():
    url = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(url) == 'https://youtu.be/xvFZjo5PgG0'

    url = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0/"></iframe>'
    assert parse(url) == 'https://youtu.be/xvFZjo5PgG0'

    url = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(url) == 'https://youtu.be/xvFZjo5PgG0'

def test_invalid():
    url = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(url) == None

    url = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZj**PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(url) == None