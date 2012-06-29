#!/usr/bin/python3

import os, shutil, zipfile, errno, re, io, codecs
from bs4 import BeautifulSoup

def main():
    div_finder = re.compile('pg_[1-9]*_mag_[1-9]*')
    soup = BeautifulSoup()
    listing =  os.listdir('files')
    for a in range(len(listing)):
        file = listing[a-1]
        file_loc = 'files/' + file
        output = load_file(file_loc)
        divs = output.findAll(attrs = {'class': div_finder})
        for a in range(len(divs)):
            insertion_point = divs[a]
            sourceID = insertion_point['class'][0]
            targetID = sourceID + '_target'
            ordinal = a + 1
            inner_div = output.new_tag("div", id = sourceID)
            json_tag = output.new_tag("a")
            json_tag['class'] = 'app-amzn-magnify'
            json_tag['data-app-amzn-magnify'] = '{"targetId":"' + targetID + '", "sourceId":"' + sourceID + '", "ordinal":' + str(ordinal) + '}'
            wrap(insertion_point.contents[1], inner_div)
            wrap(insertion_point.contents[1], json_tag)
        print(output.prettify)
            
def load_file(file_loc):
    a_content_file = codecs.open(file_loc, mode='r', encoding = 'UTF-8')
    text = a_content_file.read()
    a_content_file.close()
    output = BeautifulSoup(''.join(text))
    return output

def wrap(to_wrap, wrap_in):
    contents = to_wrap.replace_with(wrap_in)
    wrap_in.append(contents)


if __name__ == "__main__": main()