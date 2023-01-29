#données (kg)
masse_nucléon=1.67*10**-27
masse_éléctron=9.109*10**-31
#demande des numéros atomique et nombre de masse
atome=input("quel est le nom de l'atome (écrit en minucule avec les accents)si vous ne le connaissez pas mais que vous connaissez son numéro atomique écrivez 'rien'")
Z=int(input("entre le numèro atomique (si vous ne le connaissez pas écrivez '404') Z="))
if atome=='hydrogène' or Z==1:
    symbol='H'
    atome='hydrogène'
    Z=1
    A=1
    Z1=1
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis="H ."
elif atome=='lithium' or Z==3:
    atome='lithium'
    symbol='Li'
    Z=3
    A=7
    Z1=3
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis="Li ."
elif atome=='béryllium' or Z==4:
    symbol='Be'
    atome='béryllium'
    A=9
    Z=4
    Z1=4
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis="Be .."
elif atome=='sodium' or Z==11:
    symbol="Na"
    atome='sodium'
    A=23
    Z=11
    Z1=11
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis='Na .'
elif atome=='magnésium' or Z==12:
    A=24
    Z=12
    Z1=12
    atome='magnésium'
    symbol='Mg'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis='Mg ..'
elif atome=='potassium' or Z==19:
    A=39
    Z=19
    Z1=19
    atome='potassium'
    symbol='K'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis='K .'
elif atome=='calcium' or Z==20:
    A=40
    Z=20
    Z1=20
    atome='calcium'
    symbol='Ca'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis='Ca ..'
elif atome=='rubidum' or Z==37:
    A=85
    Z=37
    Z1=37
    atome='rubidum'
    symbol='Rb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis='Rb .'
#pas sur
elif atome=='sitrontium' or Z==38:
    A=88
    Z=38
    Z1=38
    atome='sitrontium'
    symbol='Sr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis='Sr ..'
elif atome=='césium' or Z==55:
    A=133
    Z=55
    Z1=55
    atome='césium'
    symbol='Cs'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis='Cs .'
elif atome=='baryum' or Z==56:
    A=138
    Z=56
    Z1=56
    atome='baryum'
    symbol='Ba'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis='Ba ..'
elif atome=='francium' or Z==87:
    A=223
    Z=87
    Z1=87
    atome='francium'
    symbol='Fr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=1
    lewis="Fr ."
elif atome=='radium' or Z==88:
    A=226
    Z=88
    Z1 = 88
    atome='radium'
    symbol='Ra'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis='Ra ..'
elif atome=='scandium' or Z==21:
    symbol='Sc'
    A=45
    Z=21
    Z1=21
    atome='scandium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis=False
elif atome=='yttrium' or Z==39:
    A=89
    Z=39
    Z1=39
    symbol='Y'
    atome='ytterium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis=False
elif atome=='lanthane' or Z==57:
    A=139
    Z=57
    Z1=57
    atome='lanthane'
    symbol='La'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis=False
elif atome=='actinium' or Z==89:
    A=227
    Z=89
    Z1=89
    symbol='Ac ...'
    atome='actinium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis=False
elif atome=='titane' or Z==22:
    A=48
    Z=22
    Z1=22
    atome='titane'
    symbol='Ti'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='zirconium' or Z==40:
    A=90
    Z=40
    Z1=40
    atome='zirconium'
    symbol='Zr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='hafnium' or Z==72:
    A=180
    Z=72
    Z1=72
    atome='hafnium'
    symbol='Hf'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='rutherfordium' or Z==104:
    A=261
    Z=104
    Z1=104
    symbol='Rf'
    atome='rutherfordium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='vanadium' or Z==23:
    A=51
    Z=23
    Z1=23
    symbol='V'
    atome='vanadium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='niobium' or Z==41:
    A=93
    Z=41
    Z1=41
    atome='nionium'
    symbol='Nb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='tantale' or Z==73:
    A=181
    Z=73
    Z1=73
    symbol='Ta'
    atome='tantale'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='dubnium' or Z==105:
    A=262
    Z=105
    Z1=105
    atome='dubnium'
    symbol='Db'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='chrome' or Z==24:
    A=52
    Z=24
    Z1=24
    atome='chrome'
    symbol='Cr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='molybdéne' or Z==42:
    A=98
    Z=42
    Z1=42
    atome='molybdéne'
    symbol='Mo'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='tungstène' or Z==74:
    A=184
    Z=74
    Z1=74
    atome='tungstène'
    symbol='W'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='seaborgium' or Z==106:
    A=266
    Z=106
    Z1=106
    atome='seaborgium'
    symbol='Sg'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='manganèse' or Z==25:
    A=55
    Z=25
    Z1=25
    symbol='Mn'
    atome='manganèse'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='technètium' or Z==43:
    Z=43
    A=98
    Z1=43
    atome='technètium'
    symbol='Tc'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='rhénium' or Z==75:
    A=187
    Z=75
    Z1=75
    atome='rhénium'
    symbol='Re'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='borhium' or Z==107:
    A=264
    Z=107
    Z1=107
    atome='borhium'
    symbol='Bh'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='fer' or Z==26:
    A=56
    Z=26
    Z1=26
    symbol='Fe'
    atome='fer'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='ruthénium' or Z==44:
    A=102
    Z=44
    Z1=44
    symbol='Ru'
    atome='ruthénium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='osmium' or Z==76:
    A=192
    Z=76
    Z1=76
    atome='osmium'
    symbol='Os'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='hassium' or Z==108:
    A=277
    Z=108
    Z1=108
    atome='hassium'
    symbol='Hs'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='cobalt' or Z==27:
    A=59
    Z=27
    Z1=27
    atome='cobalt'
    symbol='Co'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='rhodium' or Z==45:
    A=103
    Z=45
    Z1=45
    atome='rhodium'
    symbol='Rh'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='iridium' or Z==77:
    A=193
    Z=77
    Z1=77
    symbol='Ir'
    atome='iridium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='méitenerium' or Z==109:
    A=268
    Z=109
    Z1=109
    symbol='Mt'
    atome='méitenerium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='nickel' or Z==28:
    A=58
    Z=28
    Z1=28
    atome='nickel'
    symbol='Ni'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='palladium' or Z==46:
    A=106
    Z=46
    Z1=46
    atome='palladium'
    symbol='Pd'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='platine' or Z==78:
    A=195
    Z=78
    Z1=78
    atome='platine'
    symbol='Pt'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='darmstadium' or Z==110:
    A=271
    Z=110
    Z1=110
    atome='darmstadium'
    symbol='Ds'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='cuivre' or Z==29:
    A=63
    Z=29
    Z1=29
    atome='cuivre'
    symbol='Cu'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='argent' or Z==47:
    A=107
    Z=47
    Z1=47
    symbol='Ag'
    atome='argent'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='or' or Z==79:
    A=197
    Z=79
    Z1=79
    symbol='Au'
    atome='or'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='roentgénium' or Z==111:
    A=272
    Z=111
    Z1=111
    symbol='Rg'
    atome='roentgénium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='zinc' or Z==30:
    A=64
    Z=30
    Z1=30
    symbol='Zn'
    atome='zinc'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='cadmium' or Z==48:
    A=114
    Z=48
    Z1=48
    atome='cadmium'
    symbol='Cd'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='mercure' or Z==80:
    A=202
    Z=80
    Z1=80
    atome='mercure'
    symbol='Hg'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='coprnicium' or Z==112:
    A=285
    Z=112
    Z1=112
    atome='coprnicium'
    symbol='Cn'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='bore' or Z==5:
    A=11
    Z=5
    Z1=5
    atome='bore'
    symbol='B'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis="B ..."
elif atome=='aluminium' or Z==13:
    A=27
    Z=13
    Z1=13
    atome='aluminium'
    symbol='Al'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis="Al ..."
elif atome=='gallium' or Z==31:
    A=69
    Z=31
    Z1=31
    symbol='Ga'
    atome='gallium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis="Ga ..."
elif atome=='indium' or Z==49:
    A=115
    Z=49
    Z1=49
    atome='indium'
    symbol='In'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis="In ..."
elif atome=='thallium' or Z==81:
    A=205
    Z=81
    Z1=81
    atome='thallium'
    symbol='Tl'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis= "Tl ..."
elif atome=='nihonium' or Z==113:
    A=284
    Z=113
    Z1=113
    atome='nihonium'
    symbol='Nh'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=3
    lewis="Nh ..."
elif atome=='carbone' or Z==6:
    Z=6
    A=12
    Z1=6
    atome='carbone'
    symbol='C'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="C ...."
elif atome=='sillicium' or Z==14:
    A=28
    Z=14
    Z1=14
    atome='sillicium'
    symbol='Si'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="Si ...."
elif atome=='germanium' or Z==32:
    A=74
    Z=32
    Z1=32
    symbol='Ge'
    atome='germanium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="Ge ...."
elif atome=='étain' or Z==50:
    A=120
    Z=50
    Z1=50
    atome='étain'
    symbol='Sn'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="Sn ...."
elif atome=='plomb' or Z==82:
    A=208
    Z=82
    Z1=82
    atome='plomb'
    symbol='Pb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="Pb ...."
elif atome=='flévorium' or Z==114:
    A=289
    Z=114
    Z1=114
    atome='flévorium'
    symbol='Fl'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis="Fl ...."
elif atome=='azote' or Z==7:
    A=14
    Z=7
    Z1=7
    atome='azote'
    symbol='N'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis="N :..."
elif atome=='phosphore' or Z==15:
    A=31
    Z=15
    Z1=15
    atome='phosphore'
    symbol='P'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis='P :...'
elif atome=='arsenic' or Z==33:
    A=75
    Z=33
    Z1=33
    atome='arsenic'
    symbol='As'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis="As :..."
elif atome=='antimoine' or Z==51:
    A=121
    Z=51
    Z1=51
    atome='antimoine'
    symbol='Sb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis="Sb :..."
elif atome=='bismuth' or Z==83:
    A=209
    Z=83
    Z1=83
    atome='bismuth'
    symbol='Bi'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis="Bi :..."
elif atome=='moscovium' or Z==115:
    symbol='Mc'
    A=288
    Z=115
    Z1=115
    atome='moscovium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis="MC :..."
elif atome=='oxygène' or Z==8:
    A=16
    Z=8
    Z1=8
    atome='oxygène'
    symbol='O'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 2, 6, 2, 2, 6, 2, 2, 2, 6, 2, 2, 2]
    config = ""
    i = 0
    while Z1 > 0:
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1-= n_el
        i += 1
    valence=6
    lewis="O ::.."
elif atome=='soufre' or Z==16:
    A=32
    Z=16
    Z1=16
    atome='soufre'
    symbol='S'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis="S ::.."
elif atome=='sélénium' or Z==34:
    A=80
    Z=34
    Z1=34
    atome='sélénium'
    symbol='Se'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis="Se ::.."
elif atome=='tellure' or Z==52:
    A=130
    Z=52
    Z1=52
    atome='tellure'
    symbol='Te'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis="Te ::.."
elif atome=='polonium' or Z==84:
    A=210
    Z=84
    Z1=84
    atome='polonium'
    symbol='Po'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis="Po ::.."
elif atome=='livermorium' or Z==116:
    A=292
    Z=116
    Z1=116
    symbol='Lv'
    atome='livermorium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis="Lv ::.."
elif atome=='fluor' or Z==9:
    A=19
    Z=9
    Z1=9
    symbol='F'
    atome='fluor'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis="F :::."
elif atome=='chlore' or Z==17:
    A=35
    Z=17
    Z1=17
    atome='chlore'
    symbol='Cl'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis="Cl :::."
elif atome=='brome' or Z==35:
    A=79
    Z=35
    Z1=35
    atome='brome'
    symbol='Br'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis="Br :::."
elif atome=='iode' or Z==53:
    A=127
    Z=53
    Z1=53
    atome='iode'
    symbol='I'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis="I :::."
elif atome=='astate' or Z==85:
    A=210
    Z=85
    Z1=85
    atome='astate'
    symbol='At'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis="At :::."
elif atome=='tennessine' or Z==117:
    A=292
    Z=117
    Z1=117
    atome='tennessine'
    symbol='Ts'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis='Ts :::.'
elif atome=='hélium' or Z==2:
    A=4
    Z=2
    Z1=2
    atome='hélium'
    symbol='He'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=2
    lewis="He :"
elif atome=='néon' or Z==10:
    A=20
    Z=10
    Z1=10
    atome='néon'
    symbol='Ne'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Ne ::::"
elif atome=='argon' or Z==18:
    A=40
    Z=18
    Z1=18
    atome='argon'
    symbol='Ar'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Ar ::::"
elif atome=='krypton' or Z==36:
    A=84
    Z=36
    Z1=36
    atome='krypton'
    symbol='Kr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Kr ::::"
elif atome=='xénon' or Z==54:
    A=129
    Z=54
    Z1=54
    symbol='Xe'
    atome='xénon'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Xe ::::"
elif atome=='radon' or Z==86:
    A=222
    Z=86
    Z1=86
    atome='radon'
    symbol='Rn'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Rn ::::"
elif atome=='organesson' or Z==118:
    A=294
    Z=118
    Z1=118
    atome='organesson'
    symbol='Og'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis="Og ::::"
elif atome=='cérium' or Z==58:
    A=139
    Z=58
    Z1=58
    atome='cérium'
    symbol='Ce'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='thorium' or Z==90:
    A=232
    Z=90
    Z1=90
    atome='thorium'
    symbol='Th'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=4
    lewis=False
elif atome=='praséodyme' or Z==59:
    A=141
    Z=59
    Z1=59
    symbol='Pr'
    atome='prasédodyme'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='protactinium' or Z==91:
    A=231
    Z=91
    Z1=91
    symbol='Pa'
    atome='protactinium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=5
    lewis=False
elif atome=='néodyme' or Z==60:
    A=142
    Z=60
    Z1=60
    atome='néodyme'
    symbol='Nd'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='uranium' or Z==92:
    A=238
    Z=92
    Z1=92
    atome='uranium'
    symbol='U'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=6
    lewis=False
elif atome=='prométhium' or Z==61:
    A=146
    Z=61
    Z1=61
    atome='prométhium'
    symbol='Pm'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='neptunium' or Z==93:
    A=237
    Z=93
    Z1=93
    atome='neptunium'
    symbol='Np'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=7
    lewis=False
elif atome=='samarium'  or Z==62:
    A=152
    Z=62
    Z1=62
    atome='samarium'
    symbol='Sm'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='plutonium' or Z==94:
    A=244
    Z=94
    Z1=94
    atome='plutonium'
    symbol='Pu'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=8
    lewis=False
elif atome=='europium' or Z==63:
    A=153
    Z=63
    Z1=63
    atome='europium'
    symbol='Eu'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='américium' or Z==95:
    A=243
    Z=95
    Z1=95
    atome='américium'
    symbol='Am'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=9
    lewis=False
elif atome=='gadolinium' or Z==64:
    A=158
    Z=64
    Z1=64
    atome='gadolinium'
    symbol='Gd'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='curium' or Z==96:
    A=247
    Z=96
    Z1=96
    symbol='Cm'
    atome='curium'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=10
    lewis=False
elif atome=='terbium' or Z==65:
    A=159
    Z=65
    Z1=65
    atome='terbium'
    symbol='Tb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='berkélium' or Z==97:
    A=247
    Z=97
    Z1=97
    atome='berkélium'
    symbol='Bk'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=11
    lewis=False
elif atome=='dysprosium' or Z==66:
    A=164
    Z=66
    Z1=66
    atome='dysprosium'
    symbol='Dy'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='californium' or Z==98:
    A=251
    Z=98
    Z1=98
    atome='californium'
    symbol='Cf'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=12
    lewis=False
elif atome=='holmium' or Z==67:
    A=165
    Z=67
    Z1=67
    atome='holmium'
    symbol='Ho'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=13
    lewis=False
elif atome=='einsteinium' or Z==99:
    A=254
    Z=99
    Z1=99
    atome='einsteinium'
    symbol='Es'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=13
    lewis=False
elif atome=='erbium' or Z==68:
    A=166
    Z=68
    Z1=68
    atome='erbium'
    symbol='Er'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=14
    lewis=False
elif atome=='ferium' or Z==100:
    A=257
    Z=100
    Z1=100
    atome='ferium'
    symbol='Fm'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=14
    lewis=False
elif atome=='thulium' or Z==69:
    A=169
    Z=69
    Z1=69
    atome='thulium'
    symbol='Tm'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=15
    lewis=False
elif atome=='mendélinium' or Z==101:
    A=258
    Z=101
    Z1=101
    atome='mendélinium'
    symbol='Md'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=15
    lewis=False
elif atome=='ytterbium' or Z==70:
    A=174
    Z=70
    Z1=70
    atome='ytterbium'
    symbol='Yb'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=16
    lewis=False
elif atome=='nobélium' or Z==102:
    A=259
    Z=102
    Z1=102
    atome='nobélium'
    symbol='No'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=16
    lewis=False
elif atome=='lutétium' or Z==71:
    A=175
    Z=71
    Z1=71
    atome='lutétium'
    symbol='Lu'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=17
    lewis=False
elif atome=='lawrencium' or Z==103:
    A=260
    Z=103
    Z1=103
    atome='lawrencium'
    symbol='Lr'
    levels = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
    n_electrons = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
    config = ""
    i = 0
    while Z1 > 0:
        if i >= len(levels):
            print("Not enough levels to fill all electrons")
            break
        n_el = min(n_electrons[i], Z1)
        if n_el > 0:
            config += levels[i] + str(n_el) + " "
            Z1 -= n_el
        i += 1
    valence=17
    lewis=False
else:
    print("vous avez surment mal orthographié ou le numéro n'existe pas")
    exit()
#calcul des masses
masse_noyau=A*masse_nucléon
masse=Z*masse_éléctron+masse_noyau
#impression des resultats
print("----------------------------------------")
print("Résultats:")
print("Votre atome est un atome de:",atome)
print("Le symbol de cette atome est:",symbol)
#impression de la structure de l'atome
print('Le nombre de protons est:',Z)
print('Le nombre de neutrons est:',A-Z)
print("Le nombres d'éléctrons est:",Z)
print("Le nombres de nucléons est:",A)
print("----------------------------------------")
#affichage des masses du noyau et de l'atome. Et affichage de ca configuration électronique
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("La masse du noyau de l'atome de",atome ,"est:",masse_noyau,'kg')
print("La masse de l'atome de",atome," est:",masse,'kg')
print("L'atome a pour configuration électronique:",config)
print("L'atome posséde",valence, "électrons de valence")
if lewis:
    print("Le schéma de lewis de l'atome est:",lewis)
else:
    print("Votre élément est un élément de transition, il a donc plusieurs schémas de lewis possible")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("-----------------")
print("insta: lopysc7")
print("-----------------")