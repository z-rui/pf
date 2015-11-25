from PIL import Image
import numpy

def field_to_image(f):
    h, w = f.shape
    cached = numpy.array(f, copy=False)
    img = Image.new('RGB', (w, h))
    maxp = minp = 0.0
    for i in range(h):
        for j in range(w):
            val = cached[i, j]
            if not numpy.isinf(val):
                if val > maxp:
                    maxp = val
                elif val < minp:
                    minp = val
    px = img.load()
    for i in range(h):
        for j in range(w):
            val = cached[i, j]
            if numpy.isinf(val):
                px[j, i] = (255, 255, 255)
            elif numpy.abs(val) < 1e-9:
                px[j, i] = (0, 0, 0)
            elif val > 0:
                px[j, i] = (int(val / maxp * 255), 0, 0)
            else:
                px[j, i] = (0, 0, int(val / minp * 255))
    return img

def find_nextstep(f, src):
    h, w = f.shape
    i, j = src
    return min(
        ((i1, j1)
        for i1 in (i-1, i, i+1) if i1 in range(h)
        for j1 in (j-1, j, j+1) if j1 in range(w)
        ), key=lambda x: f[x]
    )

def find_path(f, src, dst=None, maxattempt=None):
    path = [src]
    h, w = f.shape
    if maxattempt is None:
        maxattempt = w*h
    while maxattempt > 0 and src != dst:
        maxattempt -= 1
        src = find_nextstep(f, src)
        path.append(src)
    return path

def draw_path(img, path):
    px = img.load()
    for i, j in path:
        px[j, i] = (0, 255, 0)
