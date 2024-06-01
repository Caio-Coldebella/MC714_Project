from process import serve
import time

a = serve(frequency=1, address=50051)
b = serve(frequency=2, address=50052)
c = serve(frequency=3, address=50053)

#time.sleep(5)
a.SendMessage('Hello, World!', 'localhost:50052')

#time.sleep(7)
b.SendMessage('Another Event', 'localhost:50053')

#time.sleep(9)
c.SendMessage('Yet Another Event', 'localhost:50051')

#When removing time sleep the program will not work as expected,