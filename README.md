# CLI ID3
![GitHub repo size](https://img.shields.io/github/repo-size/jhermosillad/ID3)

Command line interface for the ID3 algorithm. 

## Examples
Use python3 to execute any example.

### Single tree
Execute ``` simpleTree.py ``` to generate the corresponding decision tree.

<img height="160" src="/data/output/menu.png">

Expected result:

<img height="160" src="/data/output/result.png"> <img height="160" src="/data/output/output.png">

Json file:
```json
{"Outlook": {"Overcast": "Yes", "Rain": {"Wind": {"Strong": "No", "Weak": "Yes"}}, "Sunny": {"Humidity": {"High": "No", "Normal": "Yes"}}}}
```

### Cross validation
Execute ``` kfoldTree.py ``` to generate the report of 10-cross validations

<img height="160" src="/data/output/result2.png">

## References

- https://www.niser.ac.in/~smishra/teach/cs460/2020/lectures/lec11_1/
- https://towardsdatascience.com/decision-trees-for-classification-id3-algorithm-explained-89df76e72df1
- https://stackoverflow.com/questions/24657384/plotting-a-decision-tree-with-pydot
