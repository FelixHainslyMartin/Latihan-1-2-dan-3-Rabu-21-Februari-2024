print("<<<      LATIHAN     >>>")
print("Result : ")

notes = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
custom_order = ["Mi", "Do", "Fa", "So", "La", "Ti", "Re"]

def custom_sort(note):
    return custom_order.index(note)

notes.sort(key=custom_sort)
print(', '.join([f'"{note}"' for note in notes]))
