traduccion={
    "JUICIOSO":"PERSONA RESPONSABLE"
    "AGUACATE":"ES UNA FRUTA"
}

palabra= input("ingresa una palabra en mayuscula")
if palabra in traduccion.keys() :
    print("su significado es",traduccion[palabra])
else:
    print("la palbra no existe")
