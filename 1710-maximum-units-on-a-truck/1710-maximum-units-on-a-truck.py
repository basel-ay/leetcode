class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: -x[1]) # Sort list of lists Descendingly based on the second item, Optimal to put the box with the most units.
        boxes = 0
        
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box # To get the remaining boxes
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
            
        return boxes

        