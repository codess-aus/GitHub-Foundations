## What is Markdown?

Markdown is a markup language that offers a lean approach to content editing by shielding content creators from the overhead of HTML. While HTML is great for rendering content exactly how it was intended, it takes up a lot of space and can be unwieldy to work with, even in small doses. Markdown offers a great compromise between the power of HTML for content description and the ease of plain text for editing.

```
This is *italic* text.
This is also _italic_ text.
```
This is *italic* text.
This is also _italic_ text.
```
This is **bold** text.
This is also __bold__ text.
```
This is **bold** text.
This is also __bold__ text.
```
_This is **italic and bold** text_ using a single underscore for italic and double asterisks for bold.
__This is bold and *italic* text__ using double underscores for bold and single asterisks for italic.
```
_This is **italic and bold** text_ using a single underscore for italic and double asterisks for bold.
__This is bold and *italic* text__ using double underscores for bold and single asterisks for italic.

To use a literal asterisk, precede it with an escape character; in GFM, that's a backslash (\). This example results in the underscores and asterisks being shown in the output.
```
\_This is all \*\*plain\*\* text\_.
```
\_This is all \*\*plain\*\* text\_.

## Declare headings
HTML provides content headings such as the \<h1> tag. In Markdown, this is supported via the \# symbol. Just use one \# for each heading level from 1 to 6.
```
# This is H1 text
## This is H2 text
###### This is H6 text
```
# This is H1 text
## This is H2 text
###### This is H6 text

## Link to images and sites
Image and site links use a similar syntax.
```
![Link an image.](../images/codess-aus.png)
```
![Link an image.](https://github.com/codess-aus/GitHub-Foundations/blob/e7e7d19be97adf1cf130f8d134ad4708e4ce6702/images/codess-aus.png)

```
[Link to Microsoft Training](/training)
```
[Link to Microsoft Training](/training)

## Make lists
You can define ordered or unordered lists. You can also define nested items through indentation.

Ordered lists start with numbers.
Unordered lists can use asterisks or dashes (-).

## Build tables
You can construct tables using a combination of pipes (|) for column breaks and dashes (-) to designate the prior row as a header.

```
First|Second
-|-
1|2
3|4
```
## Quote text
You can create blockquotes using the greater than (>) character.
```
> This is quoted text.
```
> This is quoted text.

## Fill the gaps with inline HTML
If you come across an HTML scenario not supported by Markdown, you can use that HTML inline.
```
Here is a<br />line break
```
Here is a<br />line break

## Work with code
Markdown provides default behavior for working with inline code blocks delimited by the backtick (`) character. When decorating text with this character, it's rendered as code.
```
This is `code`.
```
This is `code`.

If you have a code segment spanning multiple lines, you can use three backticks (```) before and after to create a fenced code block.

```markdown
var first = 1;
var second = 2;
var sum = first + second;
```
```javascript
var first = 1;
var second = 2;
var sum = first + second;
```
var first = 1;
var second = 2;
var sum = first + second;

## Track task lists
You can create task lists within issues or pull requests using the following syntax. These can be helpful to track progress when used in the body of an issue or pull request.
```
- [x] First task
- [x] Second task
- [ ] Third task
```
- [x] First task
- [x] Second task
- [ ] Third task

## Command	Description
/code	Inserts a Markdown code block. You choose the language.

/details	Inserts a collapsible detail area. You choose the title and content.

/saved-replies	Inserts a saved reply. You choose from the saved replies for your user account. If you add %cursor% to your saved reply, the slash command places the cursor in that location.

/table	Inserts a Markdown table. You choose the number of columns and rows.

/tasklist	Inserts a tasklist. This slash command only works in an issue description.

/template	Shows all of the templates in the repository. You choose the template to insert. This slash command works for issue templates and a pull request template.

[Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
[GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
[GitHub Markdown emojis](https://gist.github.com/rxaviers/7360908)
[Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls)
