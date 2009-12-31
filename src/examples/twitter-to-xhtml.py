#!/usr/bin/python2.6
# coding=UTF-8

'''Load the latest update for a Renjian user and leave it in an XHTML fragment'''

__author__ = 'arthraim@gmail.com'

import codecs
import getopt
import sys
import renjian

TEMPLATE = """
<div class="renjian">
  <span class="renjian-user"><a href="http://renjian.com/%s">Renjian</a>: </span>
  <span class="renjian-text">%s</span>
  <span class="renjian-relative-created-at"><a href="http://renjian.com/%s/statuses/%s">Posted %s</a></span>
</div>
"""

def Usage():
  print 'Usage: %s [options] twitterid' % __file__
  print
  print '  This script fetches a users latest renjian update and stores'
  print '  the result in a file as an XHTML fragment'
  print
  print '  Options:'
  print '    --help -h : print this help'
  print '    --output : the output file [default: stdout]'


def FetchTwitter(user, output):
  assert user
  statuses = renjian.Api().GetUserTimeline(user=user, count=1)
  s = statuses[0]
  xhtml = TEMPLATE % (s.user.screen_name, s.text, s.user.screen_name, s.id, s.relative_date)
  if output:
    Save(xhtml, output)
  else:
    print xhtml


def Save(xhtml, output):
  out = codecs.open(output, mode='w', encoding='UTF-8',
                    errors='xmlcharrefreplace')
  out.write(xhtml)
  out.close()

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:], 'ho', ['help', 'output='])
  except getopt.GetoptError:
    Usage()
    sys.exit(2)
  try:
    user = args[0]
  except:
    Usage()
    sys.exit(2)
  output = None
  for o, a in opts:
    if o in ("-h", "--help"):
      Usage()
      sys.exit(2)
    if o in ("-o", "--output"):
      output = a
  FetchTwitter(user, output)

if __name__ == "__main__":
  main()
