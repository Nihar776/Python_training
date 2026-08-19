def usd_to_inr(usd:float)->float:
    return (usd*95.73)

usd=float(input("Enter a amount in USD to get it INR equivalent: "))
print(f"${usd}=₹{usd_to_inr(usd):.2f}")