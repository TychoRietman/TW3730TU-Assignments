import os
import random
import time
from concurrent.futures import ProcessPoolExecutor


def run_chunk(number_of_points):
    """Generate random points and count how many fall inside a unit circle."""
    inside_circle = 0

    for _ in range(number_of_points):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1.0:
            inside_circle += 1

    return inside_circle


def main():
    # Number of CPU cores allocated by Slurm.
    # If not running through Slurm, use 1 core.
    workers = int(os.environ.get("SLURM_CPUS_PER_TASK", 1))

    # Total amount of computation
    total_points = 200_000_000

    points_per_worker = total_points // workers

    print("==========================================")
    print("Parallel Monte Carlo simulation")
    print("==========================================")
    print(f"CPU cores:        {workers}")
    print(f"Total points:     {total_points:,}")
    print(f"Points per core:  {points_per_worker:,}")
    print("==========================================")

    start_time = time.perf_counter()

    # Each process gets an independent part of the calculation
    with ProcessPoolExecutor(max_workers=workers) as executor:

        jobs = [
            executor.submit(run_chunk, points_per_worker)
            for _ in range(workers)
        ]

        total_inside = sum(job.result() for job in jobs)

    actual_points = points_per_worker * workers

    pi_estimate = 4.0 * total_inside / actual_points

    runtime = time.perf_counter() - start_time

    print()
    print("==========================================")
    print("RESULT")
    print("==========================================")
    print(f"Estimated pi: {pi_estimate:.10f}")
    print(f"Actual pi:    3.1415926536")
    print(f"Error:        {abs(pi_estimate - 3.1415926536):.10f}")
    print(f"Runtime:      {runtime:.3f} seconds")
    print("==========================================")


if __name__ == "__main__":
    main()