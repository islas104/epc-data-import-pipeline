from typing import List, Tuple, Set

def computeParcelPerimeters(points: List[str]) -> List[int]:
    def parse_point(point: str) -> Tuple[int, int]:
        return tuple(map(int, point.split(',')))

    def get_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def explore_parcel(start: Tuple[int, int], visited: Set[Tuple[int, int]]) -> int:
        stack = [start]
        perimeter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # Calculate sides: any neighbor that is not part of the parcel adds to the perimeter
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor not in parcel_points:
                    perimeter += 1
                elif neighbor not in visited:
                    stack.append(neighbor)

        return perimeter

    parcel_points = set(parse_point(p) for p in points)
    visited = set()
    perimeters = []

    for point in parcel_points:
        if point not in visited:
            perimeter = explore_parcel(point, visited)
            perimeters.append(perimeter)

    return perimeters

if __name__ == "__main__":
    points = ["0,0", "0,1", "0,2", "2,0", "10,10"]
    print(computeParcelPerimeters(points))  # Example use
