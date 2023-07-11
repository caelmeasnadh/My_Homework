def bankomat(summa):
    result = []
    bancnotes = [10, 20, 50, 100, 200, 500, 100]

    for id, bancnote in enumerate(bancnotes[:-1]):
        kilkist = 10
        if summa - kilkist * bancnote < 0 :
            kilkist = summa // bancnote

        my_summa = summa - kilkist * bancnote
        while my_summa % bancnotes[id+1]:
            kilkist -= 1
            my_summa = summa - kilkist * bancnote
            if not kilkist :
                break

        result.append(f'{bancnote} x {kilkist} hrn')
        summa = my_summa
        if not summa :
            break

    if summa > 0 and not summa % bancnotes[-1] :
        result.append(f"{summa // bancnotes[-1]} x {bancnote} hrn")

    return '\n'.join(result)
zapros = int(input('Enter how much money do you need : '))
print(bankomat(zapros))