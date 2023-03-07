def get_occurrences(word, lines, include_line):
    occurences = []

    for index, line in enumerate(lines, 1):
        if word.lower() in line.lower():
            occurrence = {"linha": index}

            if include_line:
                occurrence["conteudo"] = line

            occurences.append(occurrence)

    return occurences


def generate_report(word, instance, include_line):
    report = []

    for index in range(len(instance)):
        file = instance.search(index)
        file_name = file["nome_do_arquivo"]
        file_lines = file["linhas_do_arquivo"]

        occurences = get_occurrences(word, file_lines, include_line)

        if occurences:
            file_report = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurences,
            }

            report.append(file_report)

    return report


def exists_word(word, instance):
    return generate_report(word, instance, False)


def search_by_word(word, instance):
    return generate_report(word, instance, True)
