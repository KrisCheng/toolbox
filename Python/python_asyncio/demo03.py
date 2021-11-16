# demo-03, generator basic usage.
# a simple producer-consumer demo
# no lock, and single thread

def consumer(): # a generator
    r = ''
    while True:
        n = yield r # 4.each call start from here, process and return by yield keyword
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    # 1.start generator, pass outside value to generator inner
    #   should pass None for the first time, because the generator
    #   did not execute until the point where you have the yield statement,
    #   so there is nothing to do with the value.
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1 # 2.begin to produce
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 3.switch to consumer
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)