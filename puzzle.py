import os
import re
import sys
import urllib

def read_urls(filename):
    list = []
    f = open(filename, 'r')
    for line in f:
        match  = re.search(r'"GET (\S+)', line)
        if match:
            path = match.group(1)
            if 'puzzle' in path:
                list.append(path)
    return sorted(set(list))
    #print sorted(set(match(2)))

read_urls('animal_code.google.com')

def download_images(img_urls, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    index = file(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')

    num = 0
    for i in img_urls:
        url = 'https://code.google.com' + i
        img_name = 'img' + str(num)
        print 'retrieving...', url
        urllib.urlretrieve(url, os.path.join(dest_dir, img_name))

        index.write('<img src="%s">' % (img_name,))

        '''I did this at first and found more proper solution later:
        #Html_file = open("./puzzle/index.html", "a+")
        #Html_file.write('<img src=' + '"../' + img_name + '"' + '>')
        #Html_file.close()
        '''
        num = num + 1

        index.write('\n</body></html>\n')

#read_urls('./puzzle/animal_code.google.com')
#download_images(read_urls('./puzzle/animal_code.google.com'), './puzzle')

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
    main()