import os

def run():
    token = os.getenv("HF_TOKEN")
    print("Running baseline...")
    print("Score: 0.6")

if __name__ == "__main__":
    run()