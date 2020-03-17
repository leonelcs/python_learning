year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 
30.66),(2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5), 
(2008, 32.84), (2009, 33.02), (2010, 32.92)]

print ( max( year_cheese, key=lambda yc: yc[1] ))

print ( max(map( lambda yc: (yc[1], yc), year_cheese)) )
print ( max(map(lambda yc: (yc[1], yc), year_cheese))[1] )

def numbers():
    for i in range(1024):
        print(f"= {i}")
        yield i


def sum_to(n: int) -> int:
    sum: int = 0
    for i in numbers():
        if i == n: break
        sum += i
    return sum

def main():
    numbers()

if __name__ == "__main__":
    main()