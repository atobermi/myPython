generieren .md und .html file aus csv file

```
h1=jalsdfkasjlf
h2=afsdfasdf


h1=Python links
l=https://pep8.org/ 
t=PEP 8 — the Style Guide for Python Code
r=- Basis für Entwicklungsrichtlinie

l = link
t = text in link
r = remark (optional)

in html
<h1>{h1}</h1>
<h2>{h2}</h2>
<a href="{l}">{t}</a> {r}<br>

in md

# {h1}
## {h2}
- [{l}]({t}) {r}

- [PEP 8 — the Style Guide for Python Code](https://pep8.org/) - Basis für Entwicklungsrichtlinien 


<h2>Basis Information</h2>
<p>
<a href="https://pep8.org/">PEP 8 — the Style Guide for Python Code</a> => Basis für Entwicklungsrichtlinien</br>
```
