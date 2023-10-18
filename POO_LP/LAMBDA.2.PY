lista_alumnos=[
    {
        'nombre':'ewin',
        'edad':15,
        'hobby':'danza',
        'flakita':'melody'
    },
     {
        'nombre':'del mar',
        'edad':30,
        'hobby':'saltar',
        'flakita':'melody'
    },
      {
        'nombre':'orlando',
        'edad':14,
        'hobby':'ponchar',
        'flakita':'sami'
    },
       {
        'nombre':'jory',
        'edad':25,
        'hobby':'tirar',
        'flakita':'melody'
    },
        {
        'nombre':'jans',
        'edad':35,
        'hobby':'quemarse',
        'flakita':'hermana'
    }
]
print(f' Todos  mis alumnitos{lista_alumnos}')
fans_melody=list(filter(lambda par:par['flakita']=='melody',lista_alumnos))
print(f' los que quieren con melody {fans_melody}')

#concepto
# filter


#map → modifica
print(f' Todos  mis alumnitos{lista_alumnos}')
fans_melody=list(filter(lambda par:par['edad']>24,lista_alumnos))
print(f' los que quieren con melody {fans_melody}')

nuevo_objet=list(map(lambda par:{'nombre_alumno':par['nombre'],'germita':par['flakita']},lista_alumnos))
print(nuevo_objet)