import argparse
import sys
import unittest

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', default='127.0.0.1:8000')
    ns, args = parser.parse_known_args(namespace=unittest)
    return ns, sys.argv[:1] + args


if __name__ == "__main__":
    ns, args = parse_args()
    unittest.main(module=None, argv=args)