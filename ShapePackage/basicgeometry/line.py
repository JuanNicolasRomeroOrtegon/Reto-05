from .point import Point
#Importamos la clase Point desde el módulo Point.py 

class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)
    
    def get_start_point(self) -> Point:
        return self._start_point
    
    def set_start_point(self, start_point: Point) -> None:
        self._start_point = start_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_end_point(self) -> Point:
        return self._end_point
    
    def set_end_point(self, end_point: Point) -> None:
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_length(self) -> float:
        return self._length
    