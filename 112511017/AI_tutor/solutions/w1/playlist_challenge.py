def edit_playlist(original, commands):
    edited = original[:]
    change_log = []

    for action, song in commands:
        if action == "append":
            edited.append(song)
            change_log.append((action, song, True))
        elif song in edited:
            edited.remove(song)
            change_log.append((action, song, True))
        else:
            change_log.append((action, song, False))

    return edited, change_log
