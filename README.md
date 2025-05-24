# Reto-05
Implementación de módulos y paquetes con el código usado en el Reto-04 sobre la clase "Shape".

### Estructura del paquete: 
```
ShapePackage/
│
├── basicgeometry/
│   ├── point.py
│   ├── line.py
│   └── shape.py
│
├── rectangles/
│   ├── rectangle.py
│   └── square.py
│
└── triangles/
    ├── triangle.py
    ├── equilateral.py
    ├── isoceles.py
    ├── scalene.py
    └── trirectangle.py
```

## Descripción:
El paquete principal ShapePackage está compuesto por tres módulos, los cuales poseen importaciones entre sí para facilitar la legibilidad y estructura de los códigos.

## Importaciones Relativas desde el mismo módulo:
```python
from .point import Point
from .line import Line
from .triangle import Triangle
```
## Importaciones Relativas desde otrom módulo:
```python 
from ..basicgeometry.shape import Shape
from ..basicgeometry.point import Point
```

