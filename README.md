# Analysis of Wikipedia Vandalism 

## Abstract
Although Wikipedia is one of the Internet's most-visited websites, its reliability is often
criticized as its user-generated content model allows anyone to introduce potentially uncon-
structive content. In this investigation, viewership and editing behavior for the most popular
Wikipedia articles over a one-week period were examined. The Python package mwclient
was used to collect data from the site and non-parametric methods were used in analysis. It
was determined that neither the category of an article nor its viewership is a good predictor
of the number of unconstructive edits, and that neither the category of an article nor its
semi-protection status is a good predictor of the time required for an unconstructive edit
to be reverted. While this analysis was limited in scope to popular articles, methods for
extending this to Wikipedia articles in general are considered for future applications.

## Introduction
On November 1, 2015 the number of articles on the English-language Wikipedia reached
5,000,000 with the addition of Persoonia terminalis, about an Australian shrub.Since its
creation in 2001, Wikipedia has served as a popular resource for information, but a common concern 
about its use is its nature as the encyclopedia that anyone can
edit. Many argued that its reliability is undermined by vandalism and insertion of false
content.Indeed, Wikipedia houses an article about its own reliability, and the Wikipedia
community strives to be transparent about past problems and potential solutions.For
example, since the creation and removal of false biographical content about the journalist
John Siegenthaler, additional policies have been implemented to protect against the addi-
tion of defamatory misinformation about living persons.Other concerns have included
paid editing, whitewashing of biographical articles, and intentional misinformation, and the
community has responded with additional policies and editing guidelines to minimize the
damage caused by such editing. Likewise, in the short-run, diligent editors and automated
processes are in place to revert edits deemed unconstructive.
To investigate the nature of vandalism and its reversion on Wikipedia, **data mining**
techniques were used to collect information about the editing history of a representative
random sample of popular pages in the English-language Wikipedia's article namespace.
The goal of this investigation is to provide some quantitative metrics about the reliability
of Wikipedia as a source of information. First, the objectives will be clearly defined. Next,
the methods used for data collection will be detailed. Subsequently, for each question, the
necessary exploratory data analysis will be outlined, followed by the hypotheses, analysis,
and inference. Finally, a discussion of the findings and methods will be presented, followed
by concluding remarks.

## Objectives
While the goal of this investigation is, in essence, to answer the question \Is the content of
Wikipedia articles reliable?", such a question is more subjective than objective. However,
analyzing editing behavior can provide users of the site with some quantitative information
about its reliability. The specfic questions considered in this analysis are:

1. Are the population edit ratios among the top five portals equal? That is, is the category
of an article a good predictor of the percentage of edits that are unconstructive?

2. Is there a relationship between the number of page views and the number of reverted edits?
That is, is the viewership of an article a good predictor of the number of unconstructive
edits?

3. Is there a difference in the response time among the different portals? That is, is the
category of an article a good predictor of how long it takes for an unconstructive edit to
be reverted?

4. Is there adifference in the response time between pages that are semi-protected versus
those that are unprotected? That is, is the protection status of an article a good predictor
of how long it takes an unconstructive edit to be reverted?
The terminology used in each question statement is defined as necessary in subsequent sec-
tions.

## Data Collection

The list of the 5,000 most-viewed articles on the English Wikipedia from the week of Novem-
ber 15, 2015 (specfically, from 00:00 UTC on November 15 to 23:59 UTC on November 22)
was taken from an automatically-generated report on Wikipedia. The subset of articles
and the date range were chosen to provide a representative sample of popular articles, as
those were presumed to be the most targeted for unconstructive edits. These articles ac-
counted for 421,581,978 of Wikipedia's total page views over the week, an average of 698 per
second. Each article was then manually classified as belonging to one of the twelve portals,
roughly equivalent to categories, as defined by Wikipedia. Of these 5,000 articles, multiple
articles were removed from the analysis: they are either redirects to other articles, pages
that disambiguate among several articles with similarly named titles, or were fully protected
from editing. This left a subpopulation of 3,777 categorized articles. Among these, People
and Self (consisting primarily of biographical articles) and Culture and the Arts (consisting
of articles about film, literature, sports, etc.) were the largest, with 1,554 and 1,042 articles,
respectively; Geography and Places, History and Events, and Technology and Applied Sci-
ences contained 296, 158, and 143 articles, respectively. The remaining seven portals contain
fewer than 140 articles each.

For quantitative data on the articles, the Python package mwclient was used to interface
with the MediaWiki API. The variables collected for each observation for the one-week
period were:

- Page views: the number of non-unique page calls
- Total edits: the number of saved edits
- Reverted edits: the number of edits containing the word \revert" in the edit summary
- Protection status: whether the article was semi-protected (i.e., restricted from editing
by non-logged-in editors) or unprotected (freely editable)

- Mobile percentage: percentage of page views coming from devices identified as having
a mobile operating system

The ratio of the number of edits that were reverted as above divided by the total number
of edits over the one-week period, herein referred to as the \edit ratio", was also computed
for each article. Also, for each reverted edit, the response time was also calculated by
determining the parent ID of the reverting edit and then computing the difference in the
timestamps of the reverted edit and the reverting edit. The data was output in CSV format
to allow for analysis in R.

## Directory
In the code directory, you will find two python scripts we wrote to scrap data from Wikipedia API. Under the analysis directory, you can find the analysis report markdown. 
