from itertools import islice
import pdb, sys, os
import hashlib
import argparse
chunk = 4

folder_path = "C:\\Users\\gaurav\\trunk\\src\\inSyncQA\\TestCases\\api\\regression\\cloudapp\\text"

def trim_list(a, start=None, end=None):
  return a[start:end]

def update_list_md5sum(md5_checksum, text):
  return md5_checksum.update(text)

def update_list_md5(list1, md5_checksum):
  for x in list1:
    update_list_md5sum(md5_checksum, x)
  return md5_checksum

def get_file_line(file_path):
  count=0
  fd = open(file_path, 'r')
  while 1:
    a=[x for x in islice(fd, chunk)]
    if not a:
      break
    else:
      count=count+len(a)
  return count

def get_file_md5(file_path, start_line=0, end_line=None):
  #### Handle the case 'end_line=None'
  start_line_chunk = int(start_line/chunk)
  try :
    end_line_chunk = int(end_line/chunk)
  except TypeError:
    pass
  md5_checksum = hashlib.md5()
  fd = open(file_path, 'r')
  i = 0
  line_done = 0
  while 1:
    a = [x for x in islice(fd, chunk)]
    # pdb.set_trace()
    if i==start_line_chunk:
      a = trim_list(a, start_line-line_done)
      line_done = line_done + len(a)
      if i==end_line_chunk:
        a = trim_list(a, None, end_line-start_line+1)
        update_list_md5(a, md5_checksum)
      else:
        update_list_md5(a, md5_checksum)
      print a

    elif i<start_line_chunk:
      a = trim_list(a, None, start_line-chunk)
      update_list_md5(a, md5_checksum)
      line_done = line_done + chunk
      print a

    elif end_line_chunk == i:
      a = trim_list(a, None, end_line - line_done + 1)
      update_list_md5(a, md5_checksum)
      line_done = line_done + len(a)
      print a, line_done
      break

    elif end_line_chunk > i > start_line_chunk :
      if (i+1)*chunk - start_line >= end_line:
        a = trim_list(a, None, end_line-line_done )
        line_done = line_done + len(a)
        print a
        update_list_md5(a, md5_checksum)
      else:
        update_list_md5(a, md5_checksum)
        line_done = line_done + len(a)
        print a, line_done
    else:
      break
    i=i+1
  fd.close()
  return md5_checksum.digest()

def get_folder_md5(folder_path, start_line=0, end_line=None):
  for path, dirs, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(path, file)
      md5_checksum = get_file_md5(file_path, start_line, end_line)
      print md5_checksum
      md5_checksum1 = hashlib.md5()
      md5_checksum1.update('b\nc\nd\ne\nf\ng\n\ni\nj\nk\nl\nm\nn\no\np\nq\nr\n')
      print md5_checksum1.digest()
      if md5_checksum1.digest() == md5_checksum:
        print 'yes'
      else:
        print 'no'

def main():
  parser = argparse.ArgumentParser(description='file handling')

  parser.add_argument('-r', '--recursive', action='store_true',
                      help='recursive.')

  parser.add_argument('-d', '--depth',
                      help='depth in recursive')

  parser.add_argument('-o', '--option',  choices=['s', 'n', 't'],
                      help='options for output file.')

  parser.add_argument('-f', '--first_n_lines',
                      help='first n lines')

  parser.add_argument('-l', '--last_n_lines',
                      help='first n lines')

  parser.add_argument('-a', '--any_start_end_lines',
                      help='between any two lines.')

  responce = parser.parse_args()
  print("recursive = {}".format(responce.recursive))
  if responce.recursive:
    if folder_path:
      get_folder_md5(folder_path)

  print("depth = {}".format(responce.depth))
  print("option = {}".format(responce.option))
  print("first = {}".format(responce.first_n_lines))
  print("last = {}".format(responce.last_n_lines))
  print("any two lines = {}".format(responce.any_start_end_lines))

if __name__ == '__main__':
    main()

start_line = 16
end_line = 1
if start_line > end_line:
  print "end_line can't be greater than start_line"
  raise OverflowError


get_folder_md5(folder_path, start_line, end_line)

md5_checksum = get_file_md5('text.csv', start_line, end_line)
print md5_checksum