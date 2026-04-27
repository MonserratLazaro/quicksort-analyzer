import random
import time
import matplotlib.pyplot as plt
from quicksort import quickSort   # Import algorithm

# Function to measure times
def measure_time(array):
    array_copy = array.copy()  # Avoid modifying the original array
    start = time.time()
    quickSort(array_copy, 0, len(array_copy) - 1)
    end = time.time()
    return (end - start) * 1000  # Milliseconds

# Generate arrays and save to txt file
def generate_arrays(sizes):
    for n in sizes:
        # Random array for the best case
        array_best = random.sample(range(1, n*10), n)
        with open(f"best_{n}.txt", "w") as f:
            f.write(" ".join(map(str, array_best)))

        # Sorted array for the worst case
        array_worst = list(range(1, n+1))
        with open(f"worst_{n}.txt", "w") as f:
            f.write(" ".join(map(str, array_worst)))

# Read files and run experiment
def run_experiment(sizes):
    results = []
    for n in sizes:
        with open(f"best_{n}.txt") as f:
            array_best = list(map(int, f.read().split()))
        with open(f"worst_{n}.txt") as f:
            array_worst = list(map(int, f.read().split()))

        time_best = measure_time(array_best)
        time_worst = measure_time(array_worst)

        results.append((n, time_best, time_worst))
        print(f"n={n} | Best: {time_best:.3f} ms | Worst: {time_worst:.3f} ms")
    return results

# Plot results
def plot_results(results):
    n_values = [r[0] for r in results]
    best_times = [r[1] for r in results]
    worst_times = [r[2] for r in results]

    plt.plot(n_values, best_times, marker="o", label="Best case (O(n log n))")
    plt.plot(n_values, worst_times, marker="o", label="Worst case (O(n^2))")
    plt.xlabel("Number of elements (n)")
    plt.ylabel("Time (ms)")
    plt.title("Quick Sort - Best vs Worst Case")
    plt.legend()
    plt.grid(True)
    plt.savefig("results.png")
    plt.show()

# Main
if __name__ == "__main__":
    sizes = [10, 50, 100, 200, 300, 400, 500, 800, 996]
    generate_arrays(sizes)
    results = run_experiment(sizes)

    # Save results to file
    with open("results.txt", "w") as f:
        f.write("n\tBest(ms)\tWorst(ms)\n")
        for r in results:
            f.write(f"{r[0]}\t{r[1]:.3f}\t{r[2]:.3f}\n")

    plot_results(results)
    