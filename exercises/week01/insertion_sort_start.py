"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""


def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """
    # TODO: implementeer insertion sort
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i-1
        while j >= 0 and sequence[j] > key:
            j -= 1
        sequence[j+1] = key
    return sequence


if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:

    def bubble_sort(sequence):
        n = len(sequence)
        for i in range(n-1):
            for j in range(n-i-1):
                if(sequence[j] > sequence[j+1]):
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j] # wisselen van plaats

    def merge_sort(sequence):
        size = len(sequence)
        if size > 1:
            middle = size // 2
            left_arr = sequence[:middle]
            right_arr = sequence[middle:]
 
            merge_sort(left_arr)
            merge_sort(right_arr)
 
            p = 0
            q = 0
            r = 0
 
            left_size = len(left_arr)
            right_size = len(right_arr)
            while p < left_size and q < right_size:
                if left_arr[p] < right_arr[q]:
                    sequence[r] = left_arr[p]
                    p += 1
                else:
                    sequence[r] = right_arr[q]
                    q += 1
             
                r += 1
 
            while p < left_size:
                sequence[r] = left_arr[p]
                p += 1
                r += 1
 
            while q < right_size:
                sequence[r]=right_arr[q]
                q += 1
                r += 1

    # import random
    import random
    sequence = random.sample(range(1000), 1000)
    len(sequence)

    # import time
    import time

    sizes = [10, 100, 1000, 10000]
    for n in sizes:
        sequence = random.sample(range(n), n)

        # Bubble Sort
        sequence_bubble = sequence.copy()

        start = time.time()
        bubble_sort(sequence_bubble)
        end = time.time()

        bubble_time = end - start

        # Merge Sort
        sequence_merge = sequence.copy()

        start = time.time()
        merge_sort(sequence_merge)
        end = time.time()

        merge_time = end - start

        print(f"Aantal items: {n}")
        print(f"Bubble Sort: {bubble_time:.6f} seconden")
        print(f"Merge Sort: {merge_time:.6f} seconden")
        print()
    # ...