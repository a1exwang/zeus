import sys
import sqlite3
import binascii
import re


def check_task(task_db, info_hash_or_uri):
    m = re.match(r'urn:btih:(\w+)', info_hash_or_uri)
    if m:
        info_hash = m.groups(1)
    else:
        info_hash = info_hash_or_uri

    conn = sqlite3.connect(task_db)
    c = conn.cursor()

    bin_info_hash = binascii.unhexlify(info_hash)
    rows = c.execute(
        "SELECT COUNT(*) FROM BtTask WHERE InfoId = ?;", (bin_info_hash,)
    )
    for row in rows.fetchone():
        _n, = row
        if int(_n) > 0:
            return 0
    c.close()

    return 1


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("USAGE python ./check_task.py TaskDb.dat INFO_HASH_OR_URI")
        sys.exit(2)

    task_db, info_hash_or_uri = sys.argv[1:3]
    sys.exit(check_task(task_db, info_hash_or_uri))
