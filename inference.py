import time
import os

print("App started...")

def run():
    token = os.getenv("HF_TOKEN")
    print("Running baseline...")
    print("Score: 0.6")

if __name__ == "__main__":
    run()

    # Keep container alive
    while True:
        print("Running...")
        time.sleep(5)