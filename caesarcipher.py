import tkinter as tk

fields = ('Message', 'Ciphertext', 'Shift')

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries


def encrypt(message, shift, entries):
    result = ""


    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
    entries['Ciphertext'].delete(0, tk.END)
    entries['Ciphertext'].insert(0, result)
    
    print(result)


def decrypt(ct, shift, entries):
    result = ""

    

    for i in range(len(ct)):
        char = ct[i]

        if (char.isupper()):
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
        
    entries['Message'].delete(0, tk.END)
    entries['Message'].insert(0, result)
    print(result)


if __name__ == '__main__':
    root = tk.Tk()

    ents = makeform(root, fields)



    ents['Message'].delete(0, tk.END)
    ents['Message'].insert(0, 'shiftcipher')

    ents['Ciphertext'].delete(0, tk.END)
    ents['Ciphertext'].insert(0, 'tijgudjqifs')

    ents['Shift'].delete(0, tk.END)
    ents['Shift'].insert(0, '1')

    encryptButton = tk.Button(root, text='Encrypt', command=(lambda e=ents: encrypt(str(ents['Message'].get()), int(ents['Shift'].get()), e)))
    
    encryptButton.pack(side=tk.LEFT, padx=5, pady=5)

    b2 = tk.Button(root, text='Decrypt', command=(lambda e=ents: decrypt(str(ents['Ciphertext'].get()), int(ents['Shift'].get()), e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()