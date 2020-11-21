def cos(id, **kwargs):
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )
    print(parameters)
    print(values)

cos(1, status="ended", opis="zapamiętaj czasowniki ze strony 20")