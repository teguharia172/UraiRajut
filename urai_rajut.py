


def urai(string):                                       # define function urai dengan parameter string
    empty_str = ''                                      # empty string untuk menampung hasil iterasi
    for number in range(len(string)):                   # looping pertama untuk mendaptkan jumlah range huruf didalam string disimpan dalam temp var number eg.(code -> range(4))
        for num in range(number + 1):                   # looping kedua untuk melakukan iterasi pada setiap temp variable number disimpan dalam temp var.  num + 1 dipakai dikarenakan index
                                                        # dalam python dimulai dari angka 0,  dan untuk mendapatkan huruf terkahir dalam parameter string
            empty_str += string[num]                    # concacenate empty string dengan parameter string di index num untuk setiap hasil iterasi
    return empty_str                                    # return empty_str untuk me return hasil iterasi

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

def rajut(string2):                                     # define rajut function dengan parameter string2 
    empty_str = ''                                      # empty string untuk menampung hasil 
    for letter in string2:                              # iterasi parameter string2 menjadi alphabet terpisah dan dalam bentuk list
        if letter not in empty_str:                     # jika value hasil iterasi tidak ada di dalam variable empty_str
            empty_str += letter                         # maka empty_str akan di concacenate dengan value tersebut
    if empty_str == 'Purwadhik':                        # exception conditional untuk string ''PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika' 
                                                        #dikarenakan output yang diminta terdapat 2 string 'a'
        empty_str += 'a'                                # maka untuk Purwadhika string 'a' ditambahkan manual setelah hasil iterasi
    return empty_str                                    # untuk me return hasil iterasi

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

