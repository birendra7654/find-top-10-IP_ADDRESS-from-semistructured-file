import sys

old_key = None
old_key_count = 0
top_n = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    # print data
    # break
    if len(data) != 2:
        continue

    this_key, this_key_count = data
    # this_key = this_key.strip()

    if old_key and old_key != this_key:
        top_n[old_key] = old_key_count
        # print "%s\t%d" % (old_key, old_key_count)
        old_key_count = 0

    old_key = this_key
    old_key_count += int(this_key_count)

if old_key != None:
    top_n[old_key] = old_key_count
    # print "%s\t%d" % (old_key, old_key_count)
    print sorted(top_n.items(), key=lambda x: x[1], reverse=True)[: 10]
    # print top_n
