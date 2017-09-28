# Solutions to interview questions

- **Sub-set pairs**: Expanded solution to Google's subset pair sum question solved using if else in a list comprehension.
```C++
// Google solution in C++

[1, 2, 3, 9] // Any sub-set pair sum = 8 No
[1, 2, 4 , 4] // Any sub-set pair sum = 8 yes

bool HasPairWithSum(const vector<int> data, int sum){
  unordered_set<int>comp;//complements
  for (int value : data){
    if(comp.find(value)!=comp.end) 
      return true
      comp.add(sum-value);
    }
    return false
  }
```
- **Fibonacci sequence***: Compressed version of Fibonacci sequence generator up to s

- **FizzBuzz***: The classic interview question solved with a list comprehension
