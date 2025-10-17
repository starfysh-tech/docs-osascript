<a id="//apple_ref/doc/uid/TP40016239-CH67"></a><a id="//apple_ref/doc/uid/TP40016239-CH67-SW1"></a>

## Working with XML

The XML Suite of the System Events scripting dictionary defines several classes that make it quick and easy to read and parse XML data. The `XML file` class represents any text file containing structured XML like the example data shown in Listing 36-1.

<a id="//apple_ref/doc/uid/TP40016239-CH67-SW3"></a>
**Listing 36-1**XML: Example XML data

1. `&lt;books&gt;`
2. `&lt;book country="US"&gt;`
3. `&lt;name&gt;The Secret Lives of Cats&lt;/name&gt;`
4. `&lt;publisher&gt;Feline Press&lt;/publisher&gt;`
5. `&lt;/book&gt;`
6. `&lt;/books&gt;`

At the top level, an XML file contains an `XML data` object that’s comprised of nested `XML element` objects. Each `XML element` object has a `name` and a `value` property, and may also contain `XML attribute` objects that define additional metadata. The example code in Listing 36-2 demonstrates how to access these classes to read and parse the contents of an XML file on the Desktop that contains the XML data from Listing 36-1.

**APPLESCRIPT**

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20XML%20file%20%22~%2FDesktop%2FBook%20Data.xml%22%0A%20%20%20%20%20%20%20%20tell%20XML%20element%20%22books%22%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theBookElements%20to%20every%20XML%20element%20whose%20name%20%3D%20%22book%22%0A%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7BXML%20element%201%20of%20XML%20element%201%20of%20contents%20of%20XML%20file%20%22Macintosh%20HD%3AUsers%3AYourUserName%3ADesktop%3ABook%20Data.xml%22%20of%20application%20%22System%20Events%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20repeat%20with%20a%20from%201%20to%20length%20of%20theBookElements%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theCurrentBookElement%20to%20item%20a%20of%20theBookElements%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20XML%20element%201%20of%20XML%20element%201%20of%20contents%20of%20XML%20file%20%22Macintosh%20HD%3AUsers%3Abwaldie%3ADesktop%3ABook%20Data.xml%22%20of%20application%20%22System%20Events%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tell%20theCurrentBookElement%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20theCurrentBookElement%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22book%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20every%20XML%20element%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22name%22%2C%20%22publisher%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20every%20XML%20attribute%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22country%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20of%20every%20XML%20attribute%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22US%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theBookName%20to%20value%20of%20XML%20element%20%22name%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22The%20Secret%20Lives%20of%20Cats%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20thePublisher%20to%20value%20of%20XML%20element%20%22publisher%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22Feline%20Press%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20end%20tell%0Aend%20tell)

<a id="//apple_ref/doc/uid/TP40016239-CH67-SW2"></a>
**Listing 36-2**AppleScript: Using System Events to parse an XML file

1. `tell application "System Events"`
2. ` tell XML file "~/Desktop/Book Data.xml"`
3. ` tell XML element "books"`
4. ` set theBookElements to every XML element whose name = "book"`
5. ` --&gt; {XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"}`
7. ` repeat with a from 1 to length of theBookElements`
8. ` set theCurrentBookElement to item a of theBookElements`
9. ` --&gt; XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"`
11. ` tell theCurrentBookElement`
12. ` name of theCurrentBookElement`
13. ` --&gt; "book"`
15. ` name of every XML element`
16. ` --&gt; {"name", "publisher"}`
18. ` name of every XML attribute`
19. ` --&gt; {"country"}`
21. ` value of every XML attribute`
22. ` --&gt; {"US"}`
24. ` set theBookName to value of XML element "name"`
25. ` --&gt; "The Secret Lives of Cats"`
27. ` set thePublisher to value of XML element "publisher"`
28. ` --&gt; "Feline Press"`
29. ` end tell`
30. ` end repeat`
31. ` end tell`
32. ` end tell`
33. `end tell`
