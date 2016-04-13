import pdb
import json
from urlparse import urlparse, parse_qs, parse_qsl

def obtain_key(url):
  keys = []
  parse_result = urlparse(url);
  if parse_result.query == "":
    return url
  res_list = parse_qsl(parse_result.query)
  for res in res_list:
    keys.append(res[0])
  keys.sort()
  new_query = ""
  for key in keys:
    new_query += key + "&"
  new_url = "http://" + parse_result.netloc + parse_result.path \
        + "?" + new_query
  return new_url

def has_query(url):
  parse_result = urlparse(url);
  if parse_result.query == "":
    return False
  else:
    return True

if __name__ == '__main__':
  test_url = "http://www2.shengda.edu.cn/ytw/tuanxiao/link.asp?action=go&fl_id=12"
  new_url = obtain_key(test_url)
  print "test_url: "+test_url
  print "new_url: "+new_url
