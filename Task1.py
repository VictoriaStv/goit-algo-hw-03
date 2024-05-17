import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            dest_subdir = os.path.join(dest_dir, os.path.splitext(file)[1].strip('.').lower())
            os.makedirs(dest_subdir, exist_ok=True)
            dest_path = os.path.join(dest_subdir, file)
            try:
                shutil.copy(src_path, dest_path)
                print(f"Копіювання {src_path} до {dest_path}")
            except Exception as e:
                print(f"Помилка копіювання {src_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Копіює файли з вихідної директорії до нової директорії та сортує їх за розширенням.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
