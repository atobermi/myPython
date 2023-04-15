# Tips



- [revisiting-rock-paper-scissors-in-python](https://davidamos.dev/revisiting-rock-paper-scissors-in-python/) - frozen set or tuple as dictionary keys

Sets like {"rock", "rock"} can't exist. Sets can't have repeated elements. In a real scenario, this set would look like {"rock"}. 
You don't actually need to worry about this too much. I wrote those sets with two elements to make it clear what those states represent.
You can't use sets as dictionary keys. But we want to use sets because they take care of commutativity for us automatically. 
That is, {"rock", "paper"} and {"paper", "rock"} evaluate equal to each other and should therefore return the same result upon lookup.
The way to get around this is to use Python's built-in frozenset type. Like sets, frozensets support membership checks, and 
they compare equal to another set or frozenset if and only if both sets have the same members. Unlike standard sets, however, frozenset 
instances are immutable. As a result, they can be used as dictionary keys.
