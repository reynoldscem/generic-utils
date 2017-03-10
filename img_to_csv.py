from PIL import Image
import numpy as np
import argparse
import os


def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '--input-filename',
        required=True,
        type=str
    )

    parser.add_argument(
        '-o', '--output-filename',
        required=True,
        type=str
    )

    return parser


def main():
    args = build_parser().parse_args()
    assert os.path.isfile(args.input_filename)

    img = np.array(Image.open(args.input_filename))
    design_matrix = img.reshape(np.prod(img.shape[:2]), -1)

    header = 'R,G,B'
    np.savetxt(
        os.path.abspath(args.output_filename), design_matrix,
        fmt='%i', delimiter=',', header=header, comments=''
    )

if __name__ == '__main__':
    main()
