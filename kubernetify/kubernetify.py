def kubernetify(string_to_kubernetify:str):
    kubernetified_string = ""

    for word in string_to_kubernetify.split(" "):
        if kubernetified_string != "":
            kubernetified_string += " "

        if len(word) > 2:
            kubernetified_string += word[0] + str(len(word)-2) + word[-1:]
        else:
            kubernetified_string += word

    return kubernetified_string
