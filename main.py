from copy import deepcopy


difficulty = [1, 8, 9, 10]


def generate_core_distributions(difficulty: list[int]) -> dict[tuple[int, int, int], tuple[int, int, int]]:
    core_distributions = {}
    for i in range(len(difficulty)):
        for j in range(len(difficulty)):
            for k in range(len(difficulty)):
                if i != j and j != k and i != k:
                    core_distributions[(i, j, k)] = (difficulty[i], difficulty[j], difficulty[k])
    return core_distributions


def generate_full_distributions(
    difficulty: list[int],
    core_distributions: dict[tuple[int, int, int], tuple[int, int, int]]
) -> list[dict[int, list[int]]]:
    full_distributions = []
    for core_i, core_distr in core_distributions.items():
        new_distributions = [{p: [distr_value] for p, distr_value in enumerate(core_distr)}]
        for i, elem in enumerate(difficulty):
            if i not in core_i:
                temp_distributions = []
                for s in range(3):
                    for distribution in new_distributions:
                        new_distribution = deepcopy(distribution)
                        new_distribution[s].append(elem)
                        temp_distributions.append(new_distribution)
                new_distributions = temp_distributions
        full_distributions.extend(new_distributions)

    return full_distributions


def find_max_difficulty(distributions: list[dict[int, list[int]]]) -> tuple[int, dict[int, list[int]]]:
    max_difficulty = 0
    max_distribution = None
    for distribution in distributions:
        current_difficulty = 0
        for el_1 in distribution[0]:
            for el_2 in distribution[1]:
                for el_3 in distribution[2]:
                    current_difficulty = abs(el_1 - el_2) + abs(el_2 - el_3)
                    if current_difficulty > max_difficulty:
                        max_difficulty = current_difficulty
                        max_distribution = distribution
    return max_difficulty, max_distribution


def main():
    core_distributions = generate_core_distributions(difficulty)
    full_distributions = generate_full_distributions(difficulty, core_distributions)
    max_difficulty, max_distribution = find_max_difficulty(full_distributions)
    print(f"Maximum difficulty: {max_difficulty}")
    print(f"Max distribution: {max_distribution}")


if __name__ == "__main__":
    main()