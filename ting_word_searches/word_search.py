def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        file = instance.search(index)

        file_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index, line in enumerate(file["linhas_do_arquivo"], 1):
            if word.lower() in line.lower():
                file_result["ocorrencias"].append({"linha": index})

        if file_result["ocorrencias"]:
            result.append(file_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
