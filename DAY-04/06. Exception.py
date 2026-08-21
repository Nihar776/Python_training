class dumbUserError(Exception):
    def __init__(self, num):
        if num == 0:
            super().__init__("Are you dumb!? Denominator cannot be 0 (zero)")
        else:
            super().__init__("")


try:
    p, q = map(int, input("Enter two usual numbers: ").split())

    if q == 0:
        raise dumbUserError(q)

    print(p / q)

except dumbUserError as e:
    print(e)
