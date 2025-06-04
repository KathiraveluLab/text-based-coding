from time import sleep
import traceback

try:
    print(2/0)
except ZeroDivisionError:
    print("Dividing by Zero? You mad bro?")
    traceback.print_exc()
try:
    with open("output.json", 'r') as f:
        f.write("name: Brian")
except IOError as e:
    print("The file is not hereeee:", e)
    traceback.print_exc()
finally:
    print("Closing the open file now.....")
    f.close()

try:
    with open("health.py", 'r') as f:
        for line in f:
            print(line)
except IOError as e:
    print("The file is not hereeee:", e)
    traceback.print_exc()
finally:
    print("Closing the open file now.....")
    f.close()

print("oooops")


