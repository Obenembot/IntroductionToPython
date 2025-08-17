import numpy as np
import pandas as pd


# np.random.seed(42)  # for reproducibility

def create_population(size):
    """Create a population of individuals with random fitness levels."""
    return np.random.choice([0, 1, 2], size=size)


# Step 1: Assign random fitness levels
fitness_levels = create_population(15)

print(fitness_levels)


def create_generation():
    means = {0: 6000, 1: 7500, 2: 9000}
    stds = {0: 600, 1: 500, 2: 700}

    dataset = np.zeros((15, 14), dtype=int)

    for i, level in enumerate(fitness_levels):
        steps = np.random.normal(means[level], stds[level], 14)
        steps = np.round(steps).astype(int)
        steps = np.clip(steps, 3000, 15000)  # realistic bounds
        dataset[i] = steps

    return dataset


dataset = create_generation()


def store_data_frame(data):
    columns = [f"Step_{i + 1}" for i in range(data.shape[1])]
    df = pd.DataFrame(data, columns=columns)
    return df


print("DataFrame with fitness levels as rows:")
# print(store_data_frame(create_generation()))
df = store_data_frame(create_generation())

# def store_data_frame_with_fitness(data, fitness):
print("Fitness Levels:", {f"Participant_{i + 1}": level for i, level in enumerate(fitness_levels)})
print("\nFull Dataset:\n", df)

print("\nTop 5 Participants by Fitness Level:")


def top_fitness_participants():
    avg_steps = df.mean(axis=1)
    top5_avg = avg_steps.sort_values(ascending=False).head(5)
    print("\nTop 5 Participants by Average Steps:\n", top5_avg)


top_fitness_participants()
# descending
print("over_all_mean_std:")

dataset = create_generation()
def over_all_mean_std():
    overall_mean = int(np.round(dataset.mean()))
    overall_std = int(np.round(dataset.std()))
    print("\nOverall Mean:", overall_mean)
    print("Overall Std Dev:", overall_std)


over_all_mean_std()

print("Median and Mode of Each Participant's Steps:")
def median_mode_per_participant():
    median_steps = df.median(axis=1)
    highest_median = (median_steps.idxmax(), int(median_steps.max()))
    lowest_median = (median_steps.idxmin(), int(median_steps.min()))

    print("\nHighest Median:", highest_median)
    print("Lowest Median:", lowest_median)

median_mode_per_participant()
def count_above_average():
    avg_steps = df.mean(axis=1)
    above_8000_count = (avg_steps > 8000).sum()
    print("\nParticipants with Avg > 8000 steps:", above_8000_count)

print("count_above_average:")
count_above_average()
print("percentile_steps:")
def percentile_steps():
    percentiles = np.percentile(dataset, [25, 50, 75]).astype(int)
    print("\nPercentiles (25th, 50th, 75th):", percentiles)

percentile_steps()