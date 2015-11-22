# Potential Field

Calculating the potential field and path planning.

## Dependencies

* Python (tested on 3.5)
* PIL
* numpy

## Files

* `pf.py`: General Operations.
  * Covert a potential field to an image.
  * Path planning.
  * Draw the planned path on the image.
* `epf.py`: A potential field implementation that uses Euclidean distance as potential.
  * One destination.
  * Multiple obstacles.
  * Compute the potential of any point at request.

See `example.py` for usage.
