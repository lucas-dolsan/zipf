# zipf
reads a text file and counts the amount of times every word shows up

```py zipf.py lorem_ipsum.txt```
outputs a file called ```output_lorem_ipsum.csv```
containing:
```
...
pellentesque:141
vitae:142
enim:143
egestas:147
ut:173
at:176
id:189
eget:192
amet:214
sit:215
in:234
sed:270
... and so on
```

```py plot_zipf.py output_lorem_ipsum.csv```
plots the .csv contents on a graph as shown below:
![alt text](https://i.ibb.co/HBvkhx4/lorem-ipsum-plot-output.png)
