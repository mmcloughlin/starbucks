import json
import sys


FIELDS = dict(
        store_id=int,
        name=unicode,
        city=unicode,
        country=unicode,
        latitude=float,
        longitude=float,
        )


def process_record(record):
    """
    process_record extracts selected fields from the given raw input record.
    """
    output = dict()
    for name, cast in FIELDS.items():
        if name not in record:
            return None
        output[name] = cast(record[name])
    return output


def main():
    data = json.load(sys.stdin)
    output = filter(lambda x: x is not None, map(process_record, data))
    json.dump(output, sys.stdout, indent=2)


if __name__ == '__main__':
    main()
