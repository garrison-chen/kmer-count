import sys
import os.path


def kmer_account(main_text, k):
    kmer_account = 0

    for i in range(0, len(main_text) - k + 1):
        kmer_account += 1
        # print(kmer + "\n")

    return kmer_account

'''
def unique_kmer_list(main_text, k):
    kmer_list = []

    for i in range(0, len(main_text) - k + 1):
        kmer = main_text[i: i + k]
        kmer_list.append(kmer)
        # print(kmer + "\n")
        unique_kmer_list = list(set(kmer_list))

    return unique_kmer_list
'''

main_path = sys.argv[1]
k = int(sys.argv[2]) #int(): str -> int

main_text = open(main_path, "r")
lines = main_text.readlines()

'''
main_sequence = ""
for line in lines:
    main_sequence += line.strip()
    #print(line.strip())
'''


main_text.close()

print(lines)
#print(len(main_sequence))
#print(kmer_account(main_sequence, k))
#print(len(unique_kmer_list(main_sequence, k)))
