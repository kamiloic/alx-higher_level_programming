#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """Prints the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """Parses a single line and updates total_size and status_codes."""
    parts = line.split()
    if len(parts) >= 2:
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            pass
    return total_size, status_codes


def main():
    ts = 0  # Total Size
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
    count = 0

    try:
        for line in sys.stdin:
            ts, status_codes = parse_line(line.strip(), ts, status_codes)
            count += 1
            if count % 10 == 0:
                print_stats(ts, status_codes)
    except KeyboardInterrupt:
        print_stats(ts, status_codes)
        raise


if __name__ == "__main__":
    main()
