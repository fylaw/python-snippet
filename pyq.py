from pyquery import PyQuery as pq


doc = pq(filename='hello.html')
lis = doc('li.item-0 a')
for li in lis.items():
    print(li.html())
    print(li.attr('href'))
#   print li.html()