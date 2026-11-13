"""
CLI entry point for SynthT2I.

Usage:
    python -m syntht2i [--index N] [--count N] [--length L] [--image-size N] [--max-shapes N] [--seed N] [--granularity N] [--no-color]
"""

import argparse
import sys

from .dataset import ShapeDataset


def main():
    parser = argparse.ArgumentParser(
        description="SynthT2I: Synthetic text-to-image dataset generator"
    )
    parser.add_argument(
        "--index", type=int, default=0, help="Sample index to inspect (default: 0)"
    )
    parser.add_argument(
        "--count", "-n", type=int, default=1, help="Number of consecutive captions to print starting at --index (default: 1)"
    )
    parser.add_argument(
        "--length", type=int, default=100, help="Number of samples in the dataset (default: 100)"
    )
    parser.add_argument(
        "--image-size", type=int, default=256, help="Image size in pixels (default: 256)"
    )
    parser.add_argument(
        "--max-shapes", type=int, default=3, help="Maximum shapes per image (default: 3)"
    )
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility (default: 42)"
    )
    parser.add_argument(
        "--granularity", type=int, default=8, help="Granularity for quantizing parameters (default: 8)"
    )
    parser.add_argument(
        "--no-color", action="store_true", help="Use white background (no color)"
    )

    args = parser.parse_args()

    dataset = ShapeDataset(
        length=args.length,
        image_size=args.image_size,
        max_shapes=args.max_shapes,
        seed=args.seed,
        nocolor=args.no_color,
        granularity=args.granularity,
    )

    for i in range(args.index, args.index + args.count):
        try:
            caption = dataset.get_caption(i)
        except (IndexError, ValueError) as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        print(caption)


if __name__ == "__main__":
    main()