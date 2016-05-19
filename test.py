import zip
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='test', description='')
    parser.add_argument('f')
    args = parser.parse_args()
    with zip.ZipFile(args.f, 'r') as z:
        pass
    