import pf
import epf

####################
f = epf.EuclidField(
    (50, 50),   # width x height
    (7, 14),    # goal
    [           # obstacles
        (9, 5),
        (10, 4),
        (10, 5),
        (10, 6),
        (11, 5),

        (9, 15),
        (10, 14),
        (10, 15),
        (10, 16),
        (11, 15),

        (39, 10),
        (40, 9),
        (40, 10),
        (40, 11),
        (41, 10),
    ]
)
src = (46, 5)
####################

path = pf.find_path(f, src, f.dst, 100)
im = pf.field_to_image(f)
pf.draw_path(im, path)
im.save('out.png')
