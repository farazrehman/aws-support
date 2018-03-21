
#### Cost and Usage APIs 

So this fairly new API for Cost and Usage is pretty powerful - lets you grap cost and usage related data from CLI, for examp

```
aws ce get-cost-and-usage --region us-east-1 --time-period Start=2018-01-01,End=2018-01-31 --granularity MONTHLY --metrics BlendedCost
```

Will give something this

```
{
    "ResultsByTime": [
        {
            "Estimated": false,
            "TimePeriod": {
                "Start": "2018-01-01",
                "End": "2018-01-31"
            },
            "Total": {
                "BlendedCost": {
                    "Amount": "235.8678781659",
                    "Unit": "USD"
                }
            },
            "Groups": []
        }
    ]
}
```
