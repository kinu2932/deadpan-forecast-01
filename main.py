import os

ENTRY = "New Bumbershoot: 2.3 inches of rain falling uphill at 14 mph, fog apologizing for low visibility, and a 60% chance your umbrella leaves you for someone drier."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
