import System.color as Fore
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


def bockedseatsp():
    print(Fore.BrightYellow+"--------------------------------------")
    for i in booked_seats:
        print(f"Row: {i[0]}, Seat: {i[1]}")
    print(Fore.BrightYellow+"--------------------------------------")

def checkavailable(row,seat):
    bookedstatus = False
    for i in booked_seats:
        if row == i[0] and seat == i[1]:
            bookedstatus = True
            break
        else:
            bookedstatus = False
    return bookedstatus

def bookaseat(row,seat):
    bookedstatus = False
    for i in booked_seats:
        if row == i[0] and seat == i[1]:
            bookedstatus = True
            break
        else:
            bookedstatus = False
    
    if bookedstatus == False:
        booked_seats.append((row,seat))
    return bookedstatus

def cancelseat(row,seat):
    x = 0
    bookedstatus = False
    for i in booked_seats:
        if row == i[0] and seat == i[1]:
            booked_seats.pop(x)
            bookedstatus = True
            break
        else:
            bookedstatus = False
        x = x + 1
    
    return bookedstatus

def viewstatus():
    print(Fore.BrightYellow+"--------------------------------------")
    rows = [0] * 10
    for row, seat in booked_seats:
        rows[row - 1] += 1

    total_booked = sum(rows)
    print(f"The number of seats booked: {Fore.Green}{total_booked}/200")
    print(f"{Fore.Yellow}Number of seats booked per row:{Fore.Green}", rows)
    print(Fore.BrightYellow+"--------------------------------------")

def spaceCalc(lenTotal):
    return " " * (25 - int(len(lenTotal)))

def bonus():
    outmovies = []
    for moviename,date,rates in movies:
        rate = round(sum(rates) / len(rates),2)
        if rate > 6:
            outmovies.append((moviename,date,rate))
    x = sorted(outmovies,key=lambda item:item[2])
    x.reverse()
    print(Fore.BrightYellow+"--------------------------------------")
    for i in x:
        print(f'{i[0]}{spaceCalc(i[0])}      Date: {i[1]}       Rate: {i[2]} {"⭐"*round(i[2]/2)}')
    print(Fore.BrightYellow+"--------------------------------------")


