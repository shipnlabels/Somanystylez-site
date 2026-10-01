import importlib, os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from partials import page
built = []
for f in sorted(glob.glob(os.path.join(HERE, "page_*.py"))):
    mod = importlib.import_module(os.path.basename(f)[:-3])
    html = page(mod.FILENAME, mod.TITLE, mod.DESC, mod.BODY, full_doc=True)
    open(os.path.join(ROOT, mod.FILENAME), "w").write(html)
    # artifact flavour: no document wrappers (the viewer adds its own skeleton)
    os.makedirs(os.path.join(ROOT, "build", "artifact"), exist_ok=True)
    open(os.path.join(ROOT, "build", "artifact", mod.FILENAME), "w").write(page(mod.FILENAME, mod.TITLE, mod.DESC, mod.BODY, full_doc=(mod.FILENAME != "index.html")).replace("sms-promo-720p.mp4", "sms-promo-480p.mp4"))
    built.append(mod.FILENAME)
print("built:", ", ".join(built))
