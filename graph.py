from __future__ import annotations
from typing import Iterator


class Graph:
    # Матрица смежности
    __matrix: list[list[int]]
    __vertexes: list[str]

    def __init__(self):
        self.__matrix = []
        self.__vertexes = []

    def __get_vertex_index(self, v: str) -> int:
        for index, vertex in enumerate(self.__vertexes):
            if vertex == v:
                return index

        raise Exception(f'Vertex {v} is not found')

    def first(self) -> str:
        if not len(self.__vertexes):
            raise Exception('Graph is empty')

        return self.__vertexes[0]

    def next(self, v: str) -> Iterator[str]:
        idx_v = self.__get_vertex_index(v)

        for idx, way in enumerate(self.__matrix[idx_v]):
            if way:
                yield self.__vertexes[idx]

    def vertex(self):
        pass

    def add_v(self, v: str):
        if v in self.__vertexes:
            raise Exception(f'Vertex {v} is already exist')

        for row in self.__matrix:
            row.append(0)

        new_size = len(self.__matrix) + 1
        self.__matrix.append([0] * new_size)

        self.__vertexes.append(v)

    def add_e(self, src: str, dst: str):
        idx_src = self.__get_vertex_index(src)
        idx_dst = self.__get_vertex_index(dst)

        self.__matrix[idx_src][idx_dst] = 1

    def del_v(self):
        pass

    def del_e(self):
        pass

    def edit_v(self):
        pass

    def edit_e(self):
        pass

    def get_transpose(self) -> Graph:
        result = Graph()

        for v in self.__vertexes:
            result.add_v(v)

        for v in self.__vertexes:
            for dst in self.next(v):
                result.add_e(src=dst, dst=v)

        return result
