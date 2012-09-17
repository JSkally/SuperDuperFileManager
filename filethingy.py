#cuz im so gaza imma make ur files better
#real basic..this is the skeleton code doe pree

#works with large files..it prees dem in chunks so doe sweat if it takes a while

import hashlib

def hashFile(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.sha1()
    while True:
        data = fh.read(8192)
        if not data:
            break
            sha1.update(data)
    return sha1.hexdigest()

#just to see
print 'The sha1 checksum of text.txt is', hashFile('test.txt')

#gaza again