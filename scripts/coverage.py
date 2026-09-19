import os, re, glob

ROOT = "/workspace/project"
IMGDIR = os.path.join(ROOT, "assets", "img")

# collect all files on disk
disk = set()
for d in sorted(os.listdir(IMGDIR)):
    p = os.path.join(IMGDIR, d)
    if os.path.isdir(p):
        for f in os.listdir(p):
            if f.endswith(".jpg"):
                disk.add(f"{d}/{f}")
    elif d.endswith(".jpg"):
        disk.add(d)

# collect all references in built html
refs = set()
for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
    if "/work/work/" in f:
        continue
    html = open(f).read()
    for m in re.findall(r"assets/img/([^\"']+\.jpg)", html):
        refs.add(m)
        # record location for reporting
print("files on disk :", len(disk))
print("files used    :", len(refs))
unused = sorted(disk - refs)
missing = sorted(refs - disk)
print("UNUSED  :", unused)
print("MISSING :", missing)

# which project each unused belongs to
for u in unused:
    print("   unused ->", u, os.path.getsize(os.path.join(IMGDIR, u)) // 1024, "KB")