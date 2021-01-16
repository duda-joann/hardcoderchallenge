import os


def find_all_pyfiles_for_a_single_task_in_(path):
    pypath = []
    for root, dirs, files in os.walk(path, topdown = False):
        for name in files:
            if name.endswith('.py') and name.startswith('day'):
                pypath.append(os.path.join(root, name))
    return pypath


def find_sum_of_all_lines(files):
    lines_by_task = {}
    summary_lines_with_blank = 0
    summary_lines_without_blank = 0
    sum_all_words = 0

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            without_blank = len([line for line in lines if line.strip() != ""])
            with_blanks = len([line for line in lines])
            lines_by_task[file] = without_blank
            summary_lines_with_blank += without_blank
            summary_lines_without_blank += with_blanks
            for line in lines:
                words = len([word for word in line])
                sum_all_words += words

    return (summary_lines_with_blank,
            summary_lines_without_blank,
            sum_all_words,
            lines_by_task)


def find_all_words_and_unigue(files):
    all_unique_words = {}
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            words_in_line = line.split(' ')
            for word in words_in_line:
                if word in all_unique_words and word.isalpha():
                    all_unique_words[word] += 1
                else:
                    all_unique_words[word] = 1

    return all_unique_words


def get_the_most_common_words(files):
    all_words = find_all_words_and_unigue(files)
    maximum = max(all_words.values())
    for key, value in all_words.items():
        if all_words[key] == maximum:
            return maximum, key


def find_all_imported_modules_in_(files):
    all_modules = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('import') or line.startswith('from'):
                    all_modules.append(line)

    return all_modules


def get_modules(files):
    modules = []
    all_modules = find_all_imported_modules_in_(files)
    for line in all_modules:
        word = line.strip('\n').split(' ')[1]
        modules.append(word)

    return set(modules)


def main():
    #project root for all projects
    project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    files = find_all_pyfiles_for_a_single_task_in_(project_root)
    #all projects, start with day, one file  for an one day
    print(f' User ends {len(files)}  days of challenge')
    #sum of lines with blanks, lines with_out blanks and lines per day
    line, lines, all_words, per_day = find_sum_of_all_lines(files)
    print(line, lines, all_words)
    print(*per_day.items(), sep='\n')
    all_unique_words = find_all_words_and_unigue(files)
    amount = len(all_unique_words)
    print(all_unique_words)
    print(f'All unique words which are used: {amount}')
    amount, word = get_the_most_common_words(files)
    print(f'Most common word is {word}, and used {amount} times')
    #lista zaimportowanych modułów we wszystkich programach
    modules = get_modules(files)
    #liczba uzytych modułów
    print(f'All used modules {len(modules)}')
    print(*modules, sep='\n')


if __name__ == '__main__':
    main()
