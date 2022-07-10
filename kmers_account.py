import sys
import os.path


def kmer_account(main_sequence, k):
    kmer_account = 0

    for i in range(0, len(main_sequence) - k + 1):
        kmer_account += 1
        # print(kmer + "\n")

    return kmer_account


def unique_kmer_list(main_text, k):
    kmer_list = []

    for i in range(0, len(main_text) - k + 1):
        kmer = main_text[i: i + k]
        kmer_list.append(kmer)
        # print(kmer + "\n")

    unique_kmer_list = list(set(kmer_list))
    unique_kmer_list.sort()
    return unique_kmer_list


def most_abundant_kmer(main_sequence, k):
    kmer_dict = {}
    for i in range(0, len(main_sequence) - k + 1):
        kmer = main_sequence[i: i + k]
        if kmer_dict.get(kmer):
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 0
            
    most_abundant_kmer = max(kmer_dict, key = kmer_dict.get)
    return most_abundant_kmer


main_path = sys.argv[1]
k = int(sys.argv[2]) #int(): str -> int

main_text = open(main_path, "r")
lines = main_text.readlines()
line = main_text.readline()


main_sequence = ""
for line in lines:
    if line[0] != '>':
        main_sequence += line.strip()

main_text.close()


#print(lines)
print("The total length of input sequence: " + str(len(main_sequence)))
print("The total kmer count: " + str(kmer_account(main_sequence, k)))
unique_kmer_list = unique_kmer_list(main_sequence, k)
print("The total unique kmer count: " + str(len(unique_kmer_list)))
print("The lexicogrphically smallest kmer: " + str(unique_kmer_list[0]))
print("The lexicographically largest kmer: " + str(unique_kmer_list[len(unique_kmer_list)-1]))
print("The most abundant kmer: " + str(most_abundant_kmer(main_sequence, k)))