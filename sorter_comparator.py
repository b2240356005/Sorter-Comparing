import os


# Custom pseudorandom number generator with a random initial seed
class PRNG:
    def __init__(self, seed=None):
        # Use a truly random seed if no seed is provided
        if seed is None:
            seed = int.from_bytes(os.urandom(4), 'big')  # Generate a random 32-bit integer
        self.state = seed

    def randint(self, low, high):
        # Simple linear congruential generator (LCG)
        self.state = (1103515245 * self.state + 12345) % (2 ** 31)
        return low + (self.state % (high - low + 1))


# Generate logistics dataset
def generate_logistics_dataset(num_warehouses=100, max_packages=1000, seed=None):
    """Generates a logistics dataset with a random or specified seed."""
    prng = PRNG(seed)  # Initialize PRNG with the seed or a random one
    data = []
    for i in range(1, num_warehouses + 1):
        warehouse_id = f"WH-{str(i).zfill(3)}"
        priority_level = prng.randint(1, 5)
        package_count = prng.randint(0, max_packages)
        data.append([warehouse_id, priority_level, package_count])
    return data


# Save dataset to a CSV file
def save_to_csv(data, file_name):
    """Saves the dataset to a CSV file."""
    with open(file_name, "w") as file:
        # Write the header
        file.write("Warehouse_ID,Priority_Level,Package_Count\n")
        # Write each row
        for row in data:
            file.write(",".join(map(str, row)) + "\n")


######### YOUR CODE GOES HERE ---  You shoud define here two_level_sorting and the 3 sorting functions
counter = 0
def bubble_sort(dataset,check):
    global counter
    if check == 1 :
        if len(dataset) <= 1:
            return dataset
        for i in range(len(dataset)):
            for j in range(len(dataset)-1-i):
                counter += 1
                if dataset[j][1] > dataset[j+1][1]:
                    dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        return dataset
    if check == 2:
        groups = {}
        for element in dataset:
            key = element[1]
            if key not in groups:
                groups[key] = []
            groups[key].append(element)
        groups_list = []
        for element in groups:
            groups_list.append(groups[element])
        result_d = []
        for element in groups_list:
            result_d.append(bubble_sort(element, 3))
        result = [element for alt_list in result_d for element in alt_list]
        return result
    if check == 3:
        if len(dataset) <= 1:
            return dataset
        for i in range(len(dataset)):
            for j in range(len(dataset)-1-i):
                counter += 1
                if dataset[j][2] > dataset[j+1][2]:
                    dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        return dataset



def merge_sort(dataset,check):
    global counter
    if check == 1:
        if len(dataset) <= 1:
            return dataset
        middle = len(dataset) // 2
        left, right = dataset[:middle], dataset[middle:]
        return merge(merge_sort(left,1), merge_sort(right,1))
    if check == 2:
        groups = {}
        for element in dataset:
            key = element[1]
            if key not in groups:
                groups[key] = []
            groups[key].append(element)
        groups_list = []
        for element in groups:
            groups_list.append(groups[element])
        result_d = []
        for element in groups_list:
            result_d.append(merge_sort(element, 3))
        result = [element for alt_list in result_d for element in alt_list]
        return result

    if check == 3:
        if len(dataset) <= 1:
            return dataset
        middle = len(dataset) // 2
        left, right = dataset[:middle], dataset[middle:]
        return merge_alt(merge_sort(left,3), merge_sort(right,3))



def merge(left, right):
    global counter
    dataset = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            dataset.append(left[i])
            i += 1
        elif left[i][1] > right[j][1]:
            counter += 1
            dataset.append(right[j])
            j += 1
    dataset.extend(left[i:])
    dataset.extend(right[j:])
    return dataset

def merge_alt(left, right):
    global counter
    dataset = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            dataset.append(left[i])
            i += 1
        elif left[i][2] > right[j][2]:
            counter += 1
            dataset.append(right[j])
            j += 1
    dataset.extend(left[i:])
    dataset.extend(right[j:])
    return dataset

def quick_sort(dataset,check):
    global counter
    if check == 1:
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2][1]
        less = [x for x in dataset if x[1] < pivot]
        equal = [x for x in dataset if x[1] == pivot]
        greater = [x for x in dataset if x[1] > pivot]
        counter += 1
        return quick_sort(less,1) + equal + quick_sort(greater,1)
    if check == 2:
        groups = {}
        for element in dataset:
            key = element[1]
            if key not in groups:
                groups[key] = []
            groups[key].append(element)
        groups_list = []
        for element in groups:
            groups_list.append(groups[element])
        result_d = []
        for element in groups_list:
            result_d.append(quick_sort(element, 3))
        result = [element for alt_list in result_d for element in alt_list]
        return result
    if check == 3:
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2][2]
        less = [x for x in dataset if x[2] < pivot]
        equal = [x for x in dataset if x[2] == pivot]
        greater = [x for x in dataset if x[2] > pivot]
        counter += 1
        return quick_sort(less,3) + equal + quick_sort(greater,3)


def two_level_sorting(func,dataset):
    global counter
    if func == bubble_sort:
        dataset_for_2 =bubble_sort(dataset,1)
        pl_count_bubble = int(counter)
        counter = 0
        dataset_bubble = bubble_sort(dataset_for_2,2)
        pc_count_bubble = int(counter)
        counter = 0
        return dataset_bubble, pl_count_bubble , pc_count_bubble

    if func == merge_sort:
        dataset_for_2 = merge_sort(dataset,1)
        pl_count_merge = int(counter)
        counter = 0
        dataset_merge = merge_sort(dataset_for_2,2)
        pc_count_merge = int(counter)
        counter = 0
        return dataset_merge, pl_count_merge, pc_count_merge

    if func == quick_sort:
        dataset_for_2 = quick_sort(dataset,1)
        pl_count_quick = int(counter)
        counter = 0
        dataset_quick = quick_sort(dataset_for_2,2)
        pc_count_quick = int(counter)
        counter = 0
        return dataset_quick, pl_count_quick, pc_count_quick




### Your three sorting functions should have global variable named as counter. So do not return it.



#########

def write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
):
    """Write sorted results and comparisons to the output file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write("=== Bubble Sorted Results ===\n")
        # file.write(bubble_sorted.to_string() + "\n\n")
        file.write("Warehouse_ID  Priority_Level  Package_Count\n")
        file.write("-" * 40 + "\n")
        for row in bubble_sorted:
            file.write(f"{row[0]:<12}  {row[1]:<14}  {row[2]:<13}\n")
        file.write("\n")
        file.write("=== Comparison Results ===\n")
        if merge_check:
            file.write("Merge and Bubble sorts are identical.\n")
        else:
            file.write("Merge and Bubble sorts differ.\n")

        if quick_check:
            file.write("Quick and Bubble sorts are identical.\n")
        else:
            file.write("Quick and Bubble sorts differ.\n")

        file.write("\n=== Sort Performance Metrics ===\n")
        file.write(f"Bubble priority sort iteration count: {bubble_sort_pl_iterations}\n")
        file.write(f"Merge priority sort n_of right array is smaller than left: {merge_sort_pl_counter}\n")
        file.write(f"Quick priority sort recursive step count: {quick_sort_pl_counter}\n\n")

        file.write(f"Bubble package count sort iteration count: {bubble_sort_pc_iterations}\n")
        file.write(f"Merge package count n_of right array is smaller than left: {merge_sort_pc_counter}\n")
        file.write(f"Quick package count sort recursive step count: {quick_sort_pc_counter}\n")

    print(f"Results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    # File paths and dataset size
    # Specify paths for input and output files
    INPUT_FILE = "hw05_input.csv"  # Path where the generated dataset will be saved
    OUTPUT_FILE = "hw05_output.txt"  # Path where the sorted results and metrics will be saved
    SIZE = 100 # Number of warehouses in the dataset

    # Generate the dataset
    dataset = generate_logistics_dataset(SIZE,
                                        max_packages=100)  # Generate a dataset with SIZE warehouses and max_packages packages

    # Save the generated dataset to the input file
    save_to_csv(dataset, INPUT_FILE)

    ###############################################################################################################
    # Perform sorting and counting operations
    # Sort using Bubble Sort and count iterations for Priority Level (_pl_) and Package Count (_pc_)
    bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations = two_level_sorting(bubble_sort, dataset)

    # Sort using Merge Sort and count recursive steps for Priority Level and Package Count
    merge_sorted, merge_sort_pl_counter, merge_sort_pc_counter = two_level_sorting(merge_sort, dataset)

    # Sort using Quick Sort and count recursive steps for Priority Level and Package Count
    quick_sorted, quick_sort_pl_counter, quick_sort_pc_counter = two_level_sorting(quick_sort, dataset)
    ###############################################################################################################

    # Comparisons
    # Check if Merge Sort results match Bubble Sort results
    merge_check = merge_sorted == bubble_sorted

    # Check if Quick Sort results match Bubble Sort results
    quick_check = quick_sorted == bubble_sorted

    # Write results and metrics to the output file
    write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
    )
