def bankomat(summa):
    result = []
    bancnotes = [1000, 500, 200, 100, 50, 20, 10]
    for bancnote in bancnotes:
        kilkist = summa // bancnote
        while summa >= bancnote:
            summa -= bancnote
        result.append(f'{bancnote} x {kilkist}')
    print(result)
    if summa:
        print(f"Zalushok: {summa}")
bankomat(600)
