1. copy wiki file to appropriate _posts directory
2. change filename to yyyy-mm-dd-filename.md
3. add YAML header, where "summary" is the summary listed in the file:

```
---
title: filename
excerpt: summary
layout: repo
---
```

4. delete #summary ..., #labels ..., and <wiki:toc max_depth="2" /> lines
5. replace "= text =" with "# text" everywhere there is a line with "= text ="
6. Under "URL" and "Reference": change links from the format "[url linkname]" to the format "[linkname](url)"
7. Under "URL", change all url's to the new url given, with the filename added to the end.
8. remove all square brackets (ie []) that are not links to the data
9. change the change log format from:

```
|| When || What ||
|| date || change description ||
```

to:

```
When | What
---- | ----
date | change description
```

10. save the file.


Must be provided the wiki file, the appropriate _posts directory, the appropriate date, and the new url.

See the sample for any questions.