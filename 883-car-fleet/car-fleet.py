class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse=True)
        stk = []
        print(cars)
        for car in cars:
            t = (target - car[0]) / car[1]
            if not stk:
                stk.append([car, t])
            else:
                if t > stk[-1][1]:
                    stk.append([car, t])
        
        return len(stk)
            

        