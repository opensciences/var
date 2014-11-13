# Tutorial : Slurping form Old GoogleCode to New Opensoemce


## Concepts:
 
###  There are two repos
 
+ The BABY one: just for the pretty prints on the web.  Stored ina  boring Github repo.
+ The BIG one: just of the data. Much larger. 1TB. https://terapromise.csc.ncsu.edu:8443/svn/content/t

The BIG one is already populated.

You are just adding "readme-ish" files to the BABY one in some `"*.md" file in some /topic/subtopic/_posts/*md` file.

## Before you begin

You will need: 
 
 + The old wiki file  [sample](https://github.com/opensciences/var/blob/master/Import%20from%20googlecode/sample/ant.wiki). Note that this might be found in [this old import](https://github.com/opensciences/var/tree/master/wikifiles)
+ Sort out your dir. eg. `/repo/defect/ck/_posts`
+ Sort out your file name in dir; e.g. 2014-11-07-ant.md
+ Find the site of the data in the BIG  one: e.g. https://terapromise.csc.ncsu.edu:8443/svn/content/trunk/defect/ck/ant/*

##  Step 1

+ copy wiki file to appropriate _posts directory
+ change filename to yyyy-mm-dd-filename.md
+ +add YAML header, where "summary" is the summary listed in the file:

```
---
title: filename
excerpt: summary
layout: repo
---
```

## Step 2

+ delete #summary ..., #labels ..., and <wiki:toc max_depth="2" /> lines
+ replace "= text =" with "# text" everywhere there is a line with "= text ="
+ Under "URL" and "Reference": change links from the format "[url linkname]" to the format "[linkname](url)"
+ Under "URL", change all url's to the new url given, with the filename added to the end.
+ remove all square brackets (ie []) that are not links to the data
+ change the change log format from:

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

Then save and issue a pull request.



See the [sample](http://openscience.us/repo/defect/ck/ant) for any questions.
