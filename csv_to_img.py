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

    parser.add_argument(
        '--height',
        required=True,
        type=int
    )

    parser.add_argument(
        '--width',
        required=True,
        type=int
    )

    return parser


def main():
    args = build_parser().parse_args()
    assert os.path.isfile(args.input_filename)

    data = np.genfromtxt(args.input_filename, delimiter=',')

    assert len(data) == (args.width * args.height), 'Wrong shape.'

    img = data.reshape(args.height, args.width, data.shape[-1]).astype(np.uint8)
    Image.fromarray(img).save(args.output_filename)

if __name__ == '__main__':
    main()
