import sys
import csv
from time import time

start = time()
text = open(sys.argv[1], encoding="utf8").read()


print('reading {}'.format(sys.argv[1]))

MINIMUM_COUNT_LIMIT = None
try:
    if len(sys.argv) >= 3:
        MINIMUM_COUNT_LIMIT = int(sys.argv[2])
except ValueError:
    print(f'INVALID ARG: MINIMUM_COUNT_LIMIT defaulting to 0')

diff_words = []
result_list = []
counted_words = []


def filter_str_list(text=str, filter_str=list):
    filtered_str_list = []

    def filter_word(word=str, filter_str=list):
        for string in filter_str:
            if '\n' in string:
                word = word.replace(string, ' ')
            elif string in word:
                word = word.replace(string, '')
        return word.lower()


    for word in text:
        filtered_word = filter_word(word=word, filter_str=filter_str)
        if len(filtered_word) > 0:
            filtered_str_list.append(filtered_word)

    return filtered_str_list


def split_filtered_list(text_arr=list):
    
    filtered_text_arr = []

    for idx, word in enumerate(text_arr):
        if ' ' in word:
            del text_arr[idx]
            filtered_text_arr.append(word)
    
    for word in filtered_text_arr:
        for splitten_word in word.split(' '):
            text_arr.append(splitten_word)
    return text_arr


def filter_diff_words(text=str):
    diff_words = []

    for word in text:
        if word not in diff_words:
            diff_words.append(word)
        
    return diff_words


def count_words(counted_word=str, text_arr=list):
    count = 0

    for word in text_arr:
        if counted_word == word:
            count += 1

    return (counted_word, count)


def zipf(text=list):
    zipfied_list = []

    for word in diff_words:
        if word not in counted_words:
            counted_words.append(word)
            count_result = count_words(counted_word=word, text_arr=text_arr)
            
            if len(count_result) is 2:
                zipfied_list.append(count_result)

    return zipfied_list

text_arr = filter_str_list(text=text.split(' '), filter_str=['—', '-', '_', '\n', ',', '.', '!', '?', ':', ';' , ' ', '(', ')'])

diff_words = filter_diff_words(text=split_filtered_list(text_arr=text_arr))

result_list = zipf(diff_words)
print(result_list)

if MINIMUM_COUNT_LIMIT is not None:
    result_list = [val for val in result_list if val[1] > MINIMUM_COUNT_LIMIT]

result_list.sort(key=lambda val: val[1])


filename = f"output-{sys.argv[1].replace('.txt', '.csv')}"

with open(filename, "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=':')
    for val in result_list:
        writer.writerow(val)


end = time()
print(f'zipfied list written to ./{filename}')
print('runtime: {}'.format(round(end - start, 4)))