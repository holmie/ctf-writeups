#!/usr/bin/env python3
import imageio, PIL, time, os
if not os.path.exists('output'):
    os.mkdir('output')

images = []

for imnum, l in enumerate(open('fen.txt','r').readlines()):
    l = l.replace("\n", '').replace('"', '').split()
    image = []
    for lnum, dl in enumerate(l[1].split('/')):
        imageline = []
        for c in dl:
            try:
                num = int(c)
                for i in range(0, num):
                    imageline.append(0)
            except:
                imageline.append(1)

        image.append(imageline)

    imagename = "output/image-{:02d}.png".format(imnum)
    images.append(imagename)

    imageio.imwrite(imagename, image)

html = "<html><body>"
for i in images:
    html += ("""<img src='%s'>""" % i)
html += "</body></html>"
f = open('output/index.html', 'w+')
f.write(html)
f.close()
print("""Wrote %s""" % (os.path.join(os.path.abspath('output/index.html'))))
