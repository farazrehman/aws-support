### AWS provides a rich set of CLI commands to interface with support via APIs and CLI. Sometimes you just want to quickly retrive the list of all past and current cases (included resolved) with minimal information (less clutter) - Here is the one line command to do that

```
aws support describe-cases --include-resolved-cases --output table --query 'cases[*].{"Case #":displayId, Title:subject}' --no-include-communications
```


and this what the output looks would look like:



Notice that you can always adjust the level of detail and the number of cases resturned, but for most practical situations you'd simply want to get the case-Ids that you can view in detail via Console

Contact GitHub API Training Shop Blog About
