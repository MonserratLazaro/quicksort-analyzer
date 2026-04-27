# Quick Sort Performance Analyzer

A Python tool that benchmarks **Quick Sort** performance by comparing its best case (`O(n log n)`) against its worst case (`O(n²)`), generating timing data and a visual plot of the results.

## How It Works

The program is split into two files:

### `quicksort.py`
Contains the core Quick Sort implementation.

### `main.py`
Orchestrates the benchmarking experiment.

## Requirements

Make sure you have **Python 3.7+** installed. Then install the required library:

```bash
pip install matplotlib
```

## Notes

- The worst case occurs when the array is already sorted and the last element is always chosen as pivot, leading to highly unbalanced partitions.
- For larger values of `n` (e.g., > 1000), Python's default recursion limit may be reached in the worst case. You can increase it with:

```python
import sys
sys.setrecursionlimit(5000)
```
