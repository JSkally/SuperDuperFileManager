#cuz im so gaza imma make ur files better
#real basic..this is the skeleton code doe pree

#works with large files..it prees dem in chunks so doe sweat if it takes a while

import hashlib

def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

#just to see
print 'The MD5 checksum of text.txt is', md5Checksum('test.txt')