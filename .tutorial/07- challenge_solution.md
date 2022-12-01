# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=KgIOfbC3Cvk)

<details> <summary> 👀 Answer </summary>

```python
import datetime

today = datetime.date.today()

print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
  
else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)