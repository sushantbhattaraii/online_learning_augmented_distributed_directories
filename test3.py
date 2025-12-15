import random
import numpy as np
from typing import List, Tuple


def serve_requests_remove_by_id(VpAndQ):
    """
    Same procedure as before, but deletion is done by request_id.
    This is safe even if you have duplicate triples.
    """
    rng = random.Random()
    remaining = list(VpAndQ)  # work on a copy
    batches = []

    while remaining:
        n = len(remaining)
        num_to_extract = rng.randint(1, max(1, n // 2))
        print(f"num_to_extract: {num_to_extract}")

        # 2. Create a working copy of the pool so we can remove items as we pick them
        pool = list(remaining)
        random_selected_VpAndQ_pairs = []
        print(f"Attempting to extract {num_to_extract} pairs...")

        # --- Selection Logic ---
        for _ in range(num_to_extract):
            if not random_selected_VpAndQ_pairs:
                # First selection: All items in pool are valid candidates
                candidates = pool
            else:
                # Subsequent selections: Filter candidates
                # Rule: candidate's Vp must not equal the last selected Vp
                last_vp = random_selected_VpAndQ_pairs[-1][0]
                candidates = [pair for pair in pool if pair[0] != last_vp]

            # Safety Check: If we run out of valid candidates (corner case)
            if not candidates:
                print("Warning: Ran out of valid non-consecutive options early.")
                break

            # 3. Pick a random valid candidate
            choice = random.choice(candidates)
            
            # 4. Add to result and remove from the available pool
            random_selected_VpAndQ_pairs.append(choice)
            pool.remove(choice)

        print("Randomly selected Vp1 and Q1 pairs:", random_selected_VpAndQ_pairs)

        # Another random number in [1, max(1, len(random_selected_VpAndQ_pairs))]
        next_release_frequency = rng.randint(1, max(1, len(random_selected_VpAndQ_pairs) // 2))
        print(f"next_release_frequency: {next_release_frequency}")

        # Serve first next_release_frequency from subset
        served_requests = random_selected_VpAndQ_pairs[:next_release_frequency]
        print(f"served_requests: {served_requests}")

        # Delete by request_id
        served_ids = {req_id for (req_id, _, _) in served_requests}
        remaining = [t for t in remaining if t[0] not in served_ids]

        batches.append(served_requests)

    return batches


if __name__ == "__main__":

    # VpAndQ = [(1, 48, 48), (2, 35, 35), (3, 27, 27), (4, 43, 43), (5, 33, 33), (6, 83, 83), (7, 8, 8), (8, 50, 50), (9, 56, 56), (10, 55, 55), (11, 35, 35), (12, 103, 103), (13, 81, 81), (14, 105, 105), (15, 58, 58), (16, 114, 114), (17, 7, 7), (18, 26, 26), (19, 34, 34), (20, 6, 6), (21, 121, 121), (22, 99, 99), (23, 10, 10), (24, 102, 102), (25, 12, 12), (26, 31, 31), (27, 56, 56), (28, 119, 119), (29, 123, 123), (30, 5, 5), (31, 57, 57), (32, 1, 1), (33, 73, 73), (34, 9, 9), (35, 40, 40), (36, 126, 126), (37, 84, 84), (38, 71, 71), (39, 28, 28), (40, 14, 14), (41, 55, 55), (42, 118, 118), (43, 114, 114), (44, 58, 58), (45, 107, 107), (46, 55, 55), (47, 29, 29), (48, 70, 70), (49, 111, 111)]
    VpAndQ = [(1, 48, 48), (2, 35, 35), (3, 27, 27), (4, 43, 43), (5, 33, 33), (6, 83, 83), (7, 8, 8), (8, 50, 50), (9, 56, 56), (10, 55, 55), (11, 35, 35), (12, 103, 103), (13, 81, 81), (14, 105, 105), (15, 58, 58), (16, 114, 114), (17, 7, 7), (18, 26, 26), (19, 34, 34), (20, 6, 6)]
    batches = serve_requests_remove_by_id(VpAndQ)
    # for i, batch in enumerate(batches, 1):
    #     print(f"Iteration {i}: served_requests = {batch}")
    Q_actual = [t[2] for batch in batches for t in batch]
    print("Q_actual:", Q_actual)
