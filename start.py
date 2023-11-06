import os
import threading

def execute_script(name):
    os.system('python ' + name)

# Execute a.py on a thread (concurrently)
a = threading.Thread(target=execute_script, args=('face_recognizer.py',))
a.start()

# Execute b.py on a thread (concurrently)
b = threading.Thread(target=execute_script, args=('app.py',))
b.start()

# Block main execution until a.py is terminated
a.join()
# Block main execution until b.py is terminated
b.join()