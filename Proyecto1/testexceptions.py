import time

def main():
    while True:
        print('running')
        
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print('Ops!, Something is wrong :(')
         

