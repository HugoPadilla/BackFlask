from app import db
from Modelos import Estudiante2
'''
Crear

db.create_all()

estudiante = Estudiante2.Estudiante2("12825","Pedro","Perez")
estudiante2 = Estudiante2.Estudiante2("12925","clark","Kent")

db.session.add_all([estudiante,estudiante2])
db.session.commit()

Muestra todos los registros

resultado = Estudiante2.Estudiante2.query.all()
print("lOS ESTUDIANTES SON : ")
print(resultado)



resultado2 = Estudiante2.Estudiante2.query.filter_by(nombre="Edgar")
print(resultado2.all())

resultado3 = Estudiante2.Estudiante2.query.get(10)




hacer el update


resultado4 = Estudiante2.Estudiante2.query.get(10)
resultado4.nombre = "Diana"
resultado4.cedula = "78565623"
db.session.add(resultado4)
db.session.commit()

elimina registros

resultado5 = Estudiante2.Estudiante2.query.get(10)
db.session.delete(resultado5)
db.session.commit()
'''
